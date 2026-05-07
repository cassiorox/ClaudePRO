#!/usr/bin/env python3
"""
Google Ads ClaudePRO - Setup interativo
Verifica dependencias, gera refresh token via OAuth2 e testa a conexao.

Uso:
  python3 setup.py check      # Verifica .env e dependencias
  python3 setup.py oauth       # Gera refresh token via OAuth2
  python3 setup.py test        # Testa conexao com Google Ads API
  python3 setup.py full        # check + oauth (se necessario) + test
"""

import hashlib
import os
import re
import socket
import sys
import webbrowser
from urllib.parse import unquote

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
SKILL_DIR = os.path.dirname(SCRIPT_DIR)
ENV_PATH = os.path.join(SKILL_DIR, ".env")
SCOPE = "https://www.googleapis.com/auth/adwords"
SERVER = "127.0.0.1"

# Adiciona scripts/ ao path pra importar lib
sys.path.insert(0, SCRIPT_DIR)
from lib import _load_env_file, mask_token


# ---------------------------------------------------------------------------
# Check: dependencias e .env
# ---------------------------------------------------------------------------

def check_dependencies():
    """Verifica se os pacotes necessarios estao instalados."""
    missing = []
    try:
        import google.ads.googleads  # noqa: F401
    except ImportError:
        missing.append("google-ads")
    try:
        import google_auth_oauthlib  # noqa: F401
    except ImportError:
        missing.append("google-auth-oauthlib")

    if missing:
        print(f"FALTAM: {', '.join(missing)}")
        print(f"  Instale com: pip3 install {' '.join(missing)} protobuf")
        return False
    print("OK: Dependencias instaladas")
    return True


def check_env():
    """Verifica variaveis no .env e retorna dict com status."""
    _load_env_file()
    keys = [
        "GOOGLE_ADS_DEVELOPER_TOKEN",
        "GOOGLE_ADS_CLIENT_ID",
        "GOOGLE_ADS_CLIENT_SECRET",
        "GOOGLE_ADS_REFRESH_TOKEN",
        "GOOGLE_ADS_LOGIN_CUSTOMER_ID",
    ]
    status = {}
    for key in keys:
        val = os.environ.get(key)
        present = bool(val and val.strip())
        status[key] = present
        icon = "OK" if present else "FALTA"
        display = mask_token(val) if present and "TOKEN" in key else ("OK" if present else "")
        print(f"  {icon}: {key} {display}")
    return status


def cmd_check():
    """Subcomando: verifica tudo."""
    print("=== Dependencias ===")
    deps_ok = check_dependencies()
    print()
    print("=== .env ===")
    if not os.path.isfile(ENV_PATH):
        print(f"  FALTA: Arquivo .env nao encontrado em {ENV_PATH}")
        print(f"  Crie o arquivo com o template do SKILL.md")
        return
    status = check_env()
    print()

    # Resumo
    missing = [k for k, v in status.items() if not v]
    if not deps_ok:
        print("PROXIMO PASSO: Instalar dependencias (ver comando acima)")
    elif missing:
        if missing == ["GOOGLE_ADS_REFRESH_TOKEN"]:
            print("PROXIMO PASSO: Rodar 'python3 setup.py oauth' pra gerar o refresh token")
        else:
            print(f"PROXIMO PASSO: Preencher no .env: {', '.join(missing)}")
    else:
        print("TUDO OK! Rode 'python3 setup.py test' pra confirmar a conexao.")


# ---------------------------------------------------------------------------
# OAuth: gerar refresh token
# ---------------------------------------------------------------------------

def find_free_port(start=8080, end=8090):
    """Encontra uma porta livre no range."""
    for port in range(start, end + 1):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.bind((SERVER, port))
            s.close()
            return port
        except OSError:
            continue
    return None


def run_oauth():
    """Executa fluxo OAuth2 e retorna o refresh token."""
    try:
        from google_auth_oauthlib.flow import Flow
    except ImportError:
        print("ERRO: google-auth-oauthlib nao instalado.")
        print("  Instale com: pip3 install google-auth-oauthlib")
        sys.exit(1)

    _load_env_file()
    client_id = os.environ.get("GOOGLE_ADS_CLIENT_ID", "").strip()
    client_secret = os.environ.get("GOOGLE_ADS_CLIENT_SECRET", "").strip()

    if not client_id or not client_secret:
        print("ERRO: GOOGLE_ADS_CLIENT_ID e GOOGLE_ADS_CLIENT_SECRET precisam estar no .env")
        print(f"  Arquivo: {ENV_PATH}")
        sys.exit(1)

    port = find_free_port()
    if not port:
        print("ERRO: Nenhuma porta livre entre 8080-8090. Fecha algum servidor local e tenta de novo.")
        sys.exit(1)

    redirect_uri = f"http://{SERVER}:{port}"

    client_config = {
        "installed": {
            "client_id": client_id,
            "client_secret": client_secret,
            "auth_uri": "https://accounts.google.com/o/oauth2/auth",
            "token_uri": "https://oauth2.googleapis.com/token",
        }
    }

    flow = Flow.from_client_config(client_config, scopes=[SCOPE])
    flow.redirect_uri = redirect_uri

    passthrough_val = hashlib.sha256(os.urandom(1024)).hexdigest()
    authorization_url, _ = flow.authorization_url(
        access_type="offline",
        state=passthrough_val,
        prompt="consent",
        include_granted_scopes="true",
    )

    print()
    print("=" * 60)
    print("  AUTORIZACAO GOOGLE ADS")
    print("=" * 60)
    print()
    print("Abre esta URL no browser (ou ela vai abrir sozinha):")
    print()
    print(f"  {authorization_url}")
    print()
    print(f"Aguardando callback em {redirect_uri} ...")
    print()

    # Tenta abrir o browser automaticamente
    webbrowser.open(authorization_url)

    # Mini servidor para receber o callback
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind((SERVER, port))
    sock.listen(1)

    try:
        connection, _ = sock.accept()
        data = connection.recv(4096).decode("utf-8")
    except KeyboardInterrupt:
        print("\nCancelado pelo usuario.")
        sock.close()
        sys.exit(1)

    # Parse do authorization code da query string
    match = re.search(r"GET\s\/\?(.*?)\s", data)
    if not match:
        print("ERRO: Callback invalido recebido do Google.")
        connection.close()
        sock.close()
        sys.exit(1)

    params = {}
    for pair in match.group(1).split("&"):
        if "=" in pair:
            k, v = pair.split("=", 1)
            params[k] = unquote(v)

    if "error" in params:
        print(f"ERRO do Google: {params['error']}")
        connection.close()
        sock.close()
        sys.exit(1)

    code = params.get("code", "")
    if not code:
        print("ERRO: Nenhum authorization code recebido.")
        connection.close()
        sock.close()
        sys.exit(1)

    # Responde ao browser com pagina de sucesso
    html = (
        "<html><head><meta charset='utf-8'></head><body style='font-family:sans-serif;"
        "display:flex;align-items:center;justify-content:center;height:100vh;background:#FAF7F2;'>"
        "<div style='text-align:center;'>"
        "<h1 style='color:#4CAF50;'>Pronto!</h1>"
        "<p style='color:#57534E;font-size:1.2rem;'>Autorizado com sucesso. Pode fechar esta aba.</p>"
        "</div></body></html>"
    )
    response = f"HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=utf-8\r\n\r\n{html}"
    connection.sendall(response.encode())
    connection.close()
    sock.close()

    # Troca authorization code por tokens
    flow.fetch_token(code=code)
    refresh_token = flow.credentials.refresh_token

    if not refresh_token:
        print("ERRO: Google nao retornou refresh token.")
        print("  Isso acontece quando o app ja foi autorizado antes sem prompt='consent'.")
        print("  Va em https://myaccount.google.com/permissions, revogue o app, e tente novamente.")
        sys.exit(1)

    print(f"Refresh token gerado: {mask_token(refresh_token)}")
    return refresh_token


def save_refresh_token(token):
    """Salva o refresh token no .env existente."""
    if not os.path.isfile(ENV_PATH):
        print(f"ERRO: .env nao encontrado em {ENV_PATH}")
        sys.exit(1)

    with open(ENV_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    # Substitui a linha do REFRESH_TOKEN (com ou sem aspas, com ou sem valor)
    if "GOOGLE_ADS_REFRESH_TOKEN=" in content:
        content = re.sub(
            r'GOOGLE_ADS_REFRESH_TOKEN=.*',
            f'GOOGLE_ADS_REFRESH_TOKEN="{token}"',
            content,
        )
    else:
        content = content.rstrip("\n") + f'\nGOOGLE_ADS_REFRESH_TOKEN="{token}"\n'

    with open(ENV_PATH, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"Salvo em {ENV_PATH}")


def cmd_oauth():
    """Subcomando: gera refresh token e salva no .env."""
    token = run_oauth()
    print()
    save_refresh_token(token)
    print()
    print("Proximo passo: rode 'python3 setup.py test' pra confirmar a conexao.")


# ---------------------------------------------------------------------------
# Test: testar conexao
# ---------------------------------------------------------------------------

def cmd_test():
    """Subcomando: testa conexao listando contas acessiveis."""
    from lib import init_client

    print("Testando conexao...")
    client = init_client()
    service = client.get_service("CustomerService")

    try:
        response = service.list_accessible_customers()
    except Exception as e:
        print(f"ERRO: {e}")
        sys.exit(1)

    accounts = response.resource_names
    print(f"\nConexao OK! {len(accounts)} conta(s) acessivel(is):")
    for acc in accounts:
        # customers/1234567890 -> 123-456-7890
        cid = acc.split("/")[-1]
        formatted = f"{cid[:3]}-{cid[3:6]}-{cid[6:]}" if len(cid) == 10 else cid
        print(f"  {formatted}")


# ---------------------------------------------------------------------------
# Full: check + oauth + test
# ---------------------------------------------------------------------------

def cmd_full():
    """Subcomando: fluxo completo de setup."""
    print("=== 1/3 Verificando dependencias e .env ===\n")
    deps_ok = check_dependencies()
    if not deps_ok:
        sys.exit(1)

    if not os.path.isfile(ENV_PATH):
        print(f"\nERRO: .env nao encontrado em {ENV_PATH}")
        print("Crie o arquivo com o template do SKILL.md antes de continuar.")
        sys.exit(1)

    status = check_env()
    print()

    # Checa pre-requisitos do OAuth
    for key in ["GOOGLE_ADS_DEVELOPER_TOKEN", "GOOGLE_ADS_CLIENT_ID", "GOOGLE_ADS_CLIENT_SECRET"]:
        if not status.get(key):
            print(f"ERRO: {key} precisa estar preenchido antes de gerar o refresh token.")
            sys.exit(1)

    # Gera refresh token se necessario
    if not status.get("GOOGLE_ADS_REFRESH_TOKEN"):
        print("=== 2/3 Gerando refresh token ===\n")
        cmd_oauth()
        # Recarrega env depois de salvar
        os.environ.pop("GOOGLE_ADS_REFRESH_TOKEN", None)
        _load_env_file()
    else:
        print("=== 2/3 Refresh token ja existe, pulando OAuth ===\n")

    print("=== 3/3 Testando conexao ===\n")
    cmd_test()
    print()
    print("=" * 60)
    print("  SETUP COMPLETO!")
    print("=" * 60)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

COMMANDS = {
    "check": cmd_check,
    "oauth": cmd_oauth,
    "test": cmd_test,
    "full": cmd_full,
}

if __name__ == "__main__":
    if len(sys.argv) < 2 or sys.argv[1] not in COMMANDS:
        print("Uso: python3 setup.py <comando>")
        print()
        print("Comandos:")
        print("  check   Verifica dependencias e .env")
        print("  oauth   Gera refresh token via OAuth2")
        print("  test    Testa conexao com Google Ads API")
        print("  full    Fluxo completo (check + oauth + test)")
        sys.exit(1)

    COMMANDS[sys.argv[1]]()
