#!/usr/bin/env python3
"""
Meta Ads ClaudePRO - Install Wizard
Verifica dependencias, token e conectividade com a API.

Uso: python3 setup.py
"""

import os
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
SKILL_DIR = os.path.dirname(SCRIPT_DIR)
ENV_PATH = os.path.join(SKILL_DIR, ".env")

# Adiciona scripts/ ao path pra importar lib
sys.path.insert(0, SCRIPT_DIR)
from lib import _load_env_file, mask_token

ENV_TEMPLATE = """# Meta Ads ClaudePRO - Configuracao
# Os scripts leem este arquivo automaticamente. NAO precisa adicionar ao ~/.zshrc.

# OBRIGATORIO: Token de acesso da Meta (ver references/setup-meta-app.md)
META_ADS_TOKEN=""

# OBRIGATORIO: App ID do app Meta que gerou o token
META_APP_ID=""

# OPCIONAL: Conta de anuncio padrao (evita passar --account toda vez)
META_AD_ACCOUNT_ID=""
"""


def check_env_file():
    """Carrega o .env da skill. Cria a partir do template se nao existir."""
    loaded = _load_env_file()
    if loaded:
        print(f"  [OK] .env carregado de {loaded}")
        return True

    print(f"  [FALHOU] .env nao encontrado em {ENV_PATH}")
    try:
        with open(ENV_PATH, "w", encoding="utf-8") as f:
            f.write(ENV_TEMPLATE)
        os.chmod(ENV_PATH, 0o600)
        print(f"           Criei o template. Preencha e rode de novo:")
        print(f"           {ENV_PATH}")
    except OSError as e:
        print(f"           Nao consegui criar o template: {e}")
    return False


def check_python():
    v = sys.version_info
    ok = v.major >= 3 and v.minor >= 8
    status = "OK" if ok else "FALHOU"
    print(f"  [{status}] Python {v.major}.{v.minor}.{v.micro} (minimo: 3.8)")
    return ok


def check_sdk():
    try:
        import facebook_business
        version = getattr(facebook_business, '__version__', '?')
        print(f"  [OK] facebook-business SDK v{version}")
        return True
    except ImportError:
        print("  [FALHOU] facebook-business SDK nao instalado")
        print("           Instale com: pip3 install facebook-business")
        return False


def check_requests():
    try:
        import requests
        print(f"  [OK] requests v{requests.__version__}")
        return True
    except ImportError:
        print("  [FALHOU] requests nao instalado")
        print("           Instale com: pip3 install requests")
        return False


def check_token():
    token = os.environ.get("META_ADS_TOKEN")
    if not token:
        print("  [FALHOU] META_ADS_TOKEN vazia")
        print(f"           Preencha no .env: {ENV_PATH}")
        print('           META_ADS_TOKEN="seu-token-aqui"')
        print("           Como gerar o token: references/setup-meta-app.md")
        return False
    print(f"  [OK] META_ADS_TOKEN definida ({mask_token(token)})")
    return True


def check_app_id():
    app_id = os.environ.get("META_APP_ID")
    if not app_id:
        print("  [FALHOU] META_APP_ID vazia")
        print(f"           Preencha no .env: {ENV_PATH}")
        print('           META_APP_ID="123456789012345"')
        return False
    print(f"  [OK] META_APP_ID = {app_id}")
    return True


def check_account():
    account = os.environ.get("META_AD_ACCOUNT_ID")
    if not account:
        print("  [AVISO] META_AD_ACCOUNT_ID nao definida (opcional)")
        print("          Da pra definir uma conta padrao no .env:")
        print('          META_AD_ACCOUNT_ID="act_123456789"')
        return True  # Optional, not a failure
    print(f"  [OK] META_AD_ACCOUNT_ID = {account}")
    return True


def check_api_connection():
    token = os.environ.get("META_ADS_TOKEN")
    if not token:
        print("  [PULOU] Teste de API (sem token)")
        return False

    try:
        import facebook_business
    except ImportError:
        print("  [PULOU] Teste de API (sem SDK)")
        return False

    from facebook_business.api import FacebookAdsApi
    from facebook_business.adobjects.user import User

    try:
        FacebookAdsApi.init(access_token=token)
        me = User(fbid="me")
        me.remote_read(fields=["name", "id"])
        name = me.get("name", "?")
        uid = me.get("id", "?")
        print(f"  [OK] Conectado como: {name} (ID: {uid})")
        return True
    except Exception as e:
        print(f"  [FALHOU] Erro ao conectar na API: {e}")
        return False


def check_ad_accounts():
    token = os.environ.get("META_ADS_TOKEN")
    if not token:
        return False

    try:
        from facebook_business.api import FacebookAdsApi
        from facebook_business.adobjects.user import User
        FacebookAdsApi.init(access_token=token)
        me = User(fbid="me")
        accounts = me.get_ad_accounts(fields=["name", "id", "account_status"])
        acct_list = list(accounts)
        print(f"  [OK] {len(acct_list)} conta(s) de anuncio encontrada(s):")
        for acct in acct_list[:10]:
            status_map = {1: "ACTIVE", 2: "DISABLED", 3: "UNSETTLED", 7: "PENDING_RISK_REVIEW", 101: "CLOSED"}
            status = status_map.get(acct.get("account_status"), str(acct.get("account_status", "?")))
            print(f"       - {acct.get('name', '?')} ({acct.get('id')}) [{status}]")
        if len(acct_list) > 10:
            print(f"       ... e mais {len(acct_list) - 10}")
        return True
    except Exception as e:
        print(f"  [FALHOU] Erro ao listar contas: {e}")
        return False


def main():
    print("=" * 55)
    print("  Meta Ads ClaudePRO - Install Wizard")
    print("=" * 55)

    print("\n1. Dependencias:")
    py_ok = check_python()
    sdk_ok = check_sdk()
    req_ok = check_requests()

    print("\n2. Configuracao (.env):")
    env_ok = check_env_file()

    print("\n3. Autenticacao:")
    token_ok = check_token()
    app_ok = check_app_id()
    account_ok = check_account()

    print("\n4. Conectividade:")
    if sdk_ok and token_ok:
        api_ok = check_api_connection()
        if api_ok:
            check_ad_accounts()
    else:
        print("  [PULOU] Resolva dependencias e token primeiro")
        api_ok = False

    # Summary
    print("\n" + "=" * 55)
    all_ok = py_ok and sdk_ok and req_ok and token_ok and app_ok
    if all_ok and api_ok:
        print("  TUDO PRONTO! Skill meta-ads configurada.")
        print("  Use via Claude Code com linguagem natural")
        print("  ou invoque /meta-ads")
    elif all_ok:
        print("  QUASE LA! Dependencias OK mas API nao conectou.")
        print("  Verifique seu token e tente novamente.")
    else:
        print("  PENDENCIAS encontradas. Resolva os itens [FALHOU]")
        print("  e rode novamente: python3 setup.py")
    print("=" * 55)

    sys.exit(0 if (all_ok and api_ok) else 1)


if __name__ == "__main__":
    main()
