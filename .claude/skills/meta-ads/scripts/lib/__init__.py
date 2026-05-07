#!/usr/bin/env python3
"""
Meta Ads ClaudePRO - Biblioteca compartilhada
Auth, SDK init, output helpers, error handling
"""

import json
import os
import sys
import time

# ---------------------------------------------------------------------------
# Dependency check
# ---------------------------------------------------------------------------

def ensure_sdk():
    """Verifica se o facebook-business SDK esta instalado."""
    try:
        import facebook_business
        return True
    except ImportError:
        print("ERRO: SDK 'facebook-business' nao instalado.", file=sys.stderr)
        print("  Instale com: pip3 install facebook-business", file=sys.stderr)
        sys.exit(1)

# ---------------------------------------------------------------------------
# Auth & SDK init
# ---------------------------------------------------------------------------

_api_initialized = False

# ---------------------------------------------------------------------------
# .env loader (sem depender de python-dotenv)
# ---------------------------------------------------------------------------

_ENV_SEARCH_PATHS = [
    os.path.expanduser("~/.claude/skills/meta-ads/.env"),
    os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), ".env"),
]

def _load_env_file():
    """Carrega variáveis de um .env sem precisar de source no zshrc."""
    for env_path in _ENV_SEARCH_PATHS:
        if os.path.isfile(env_path):
            with open(env_path, "r", encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if not line or line.startswith("#"):
                        continue
                    # Remove 'export ' se presente
                    if line.startswith("export "):
                        line = line[7:]
                    if "=" not in line:
                        continue
                    key, _, value = line.partition("=")
                    key = key.strip()
                    value = value.strip().strip('"').strip("'")
                    # Só seta se não existir na env (env var explícita tem prioridade)
                    if key and value and not os.environ.get(key):
                        os.environ[key] = value
            return env_path
    return None


def mask_token(token):
    """Mascara token pra não vazar em logs/output. Mostra só os 6 primeiros chars."""
    if not token or len(token) < 10:
        return "***"
    return f"{token[:6]}...{token[-4:]}"


def init_api():
    """Inicializa o SDK com o token do .env ou env var META_ADS_TOKEN."""
    global _api_initialized
    if _api_initialized:
        return

    ensure_sdk()
    from facebook_business.api import FacebookAdsApi

    # Tenta carregar do .env primeiro
    env_file = _load_env_file()

    token = os.environ.get("META_ADS_TOKEN")
    if not token:
        print("ERRO: Token META_ADS_TOKEN não encontrado.", file=sys.stderr)
        print("  Crie o arquivo .claude/skills/meta-ads/.env com:", file=sys.stderr)
        print('  META_ADS_TOKEN="seu-token-aqui"', file=sys.stderr)
        print("", file=sys.stderr)
        print("  Ou rode: /meta-ads setup", file=sys.stderr)
        sys.exit(1)

    FacebookAdsApi.init(access_token=token)
    _api_initialized = True

    if env_file:
        print(f"Token carregado de {env_file} ({mask_token(token)})", file=sys.stderr)


def get_default_account_id():
    """Retorna o account ID padrao da env var META_AD_ACCOUNT_ID."""
    account_id = os.environ.get("META_AD_ACCOUNT_ID")
    if not account_id:
        print("ERRO: Nenhuma conta informada.", file=sys.stderr)
        print("  Use --account act_XXX ou defina META_AD_ACCOUNT_ID.", file=sys.stderr)
        sys.exit(1)
    if not account_id.startswith("act_"):
        account_id = f"act_{account_id}"
    return account_id


def resolve_account(args_account=None):
    """Resolve account ID: argumento CLI > env var."""
    if args_account:
        acct = args_account
        if not acct.startswith("act_"):
            acct = f"act_{acct}"
        return acct
    return get_default_account_id()

# ---------------------------------------------------------------------------
# Output helpers
# ---------------------------------------------------------------------------

def print_json(obj):
    """Serializa e printa qualquer objeto do SDK ou dict para stdout."""
    data = _serialize(obj)
    print(json.dumps(data, indent=2, ensure_ascii=False, default=str))


def _serialize(obj):
    """Converte objetos do SDK para dicts serializaveis."""
    if obj is None:
        return None
    if isinstance(obj, (str, int, float, bool)):
        return obj
    if isinstance(obj, dict):
        return {k: _serialize(v) for k, v in obj.items()}
    if isinstance(obj, (list, tuple)):
        return [_serialize(item) for item in obj]
    # SDK AbstractCrudObject
    if hasattr(obj, 'export_all_data'):
        return _serialize(obj.export_all_data())
    # SDK Cursor (iteravel paginado)
    if hasattr(obj, '__iter__') and hasattr(obj, 'params'):
        return [_serialize(item) for item in obj]
    # Fallback
    try:
        return json.loads(json.dumps(obj, default=str))
    except (TypeError, ValueError):
        return str(obj)


def print_error(msg):
    """Printa erro formatado para stderr."""
    print(f"ERRO: {msg}", file=sys.stderr)

# ---------------------------------------------------------------------------
# Error handling
# ---------------------------------------------------------------------------

def handle_fb_error(func):
    """Decorator que trata erros do SDK do Facebook."""
    def wrapper(*args, **kwargs):
        ensure_sdk()
        from facebook_business.exceptions import FacebookRequestError
        try:
            return func(*args, **kwargs)
        except FacebookRequestError as e:
            error_data = {
                "error": True,
                "message": e.api_error_message(),
                "code": e.api_error_code(),
                "subcode": e.api_error_subcode(),
                "type": e.api_error_type(),
                "fbtrace_id": e.api_transient_error() if hasattr(e, 'api_transient_error') else None,
            }
            # Rate limiting
            if e.api_error_code() in (17, 32, 80004):
                error_data["hint"] = "Rate limit atingido. Aguarde alguns minutos antes de tentar novamente."
            print(json.dumps(error_data, indent=2, ensure_ascii=False, default=str))
            sys.exit(1)
        except Exception as e:
            print_error(str(e))
            sys.exit(1)
    return wrapper

# ---------------------------------------------------------------------------
# Rate limiting helpers
# ---------------------------------------------------------------------------

def safe_delay(seconds=1):
    """Delay entre operacoes de escrita para evitar rate limiting."""
    time.sleep(seconds)

# ---------------------------------------------------------------------------
# Common argparse helpers
# ---------------------------------------------------------------------------

def add_account_arg(parser):
    """Adiciona argumento --account ao parser."""
    parser.add_argument("--account", help="Ad account ID (ex: act_123). Padrao: META_AD_ACCOUNT_ID")


def add_fields_arg(parser):
    """Adiciona argumento --fields ao parser."""
    parser.add_argument("--fields", help="Campos separados por virgula (ex: name,status,id)")


def add_pagination_args(parser):
    """Adiciona argumentos de paginacao ao parser."""
    parser.add_argument("--limit", type=int, default=None, help="Limite de resultados (padrao: todos)")
    parser.add_argument("--after", help="Cursor de paginacao (proxima pagina)")
    parser.add_argument("--before", help="Cursor de paginacao (pagina anterior)")


def add_status_filter_arg(parser):
    """Adiciona argumento --status ao parser."""
    parser.add_argument("--status", help="Filtrar por status: ACTIVE,PAUSED,ARCHIVED (separados por virgula)")


def parse_fields(fields_str):
    """Converte string 'name,status,id' em lista."""
    if not fields_str:
        return None
    return [f.strip() for f in fields_str.split(",")]


def parse_json_arg(json_str, arg_name="argumento"):
    """Faz parse de um argumento JSON string."""
    if not json_str:
        return None
    try:
        return json.loads(json_str)
    except json.JSONDecodeError as e:
        print_error(f"JSON invalido no argumento {arg_name}: {e}")
        sys.exit(1)


def parse_status_filter(status_str):
    """Converte 'ACTIVE,PAUSED' em lista de filtro de effective_status."""
    if not status_str:
        return None
    return [s.strip().upper() for s in status_str.split(",")]
