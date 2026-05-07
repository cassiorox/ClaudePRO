#!/usr/bin/env python3
"""
Google Ads ClaudePRO - Biblioteca compartilhada
Auth (google-ads SDK), .env loader, GAQL runner, output helpers, error handling
"""

import json
import os
import sys
import time

# ---------------------------------------------------------------------------
# Dependency check
# ---------------------------------------------------------------------------

def ensure_sdk():
    """Verifica se o google-ads SDK esta instalado."""
    try:
        import google.ads.googleads
        return True
    except ImportError:
        print("ERRO: SDK 'google-ads' nao instalado.", file=sys.stderr)
        print("  Instale com: pip3 install google-ads protobuf", file=sys.stderr)
        sys.exit(1)

# ---------------------------------------------------------------------------
# .env loader (sem depender de python-dotenv)
# ---------------------------------------------------------------------------

_ENV_SEARCH_PATHS = [
    os.path.expanduser("~/.claude/skills/google-ads/.env"),
    os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), ".env"),
]

_YAML_SEARCH_PATHS = [
    os.path.expanduser("~/.claude/skills/google-ads/google-ads.yaml"),
    os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), "google-ads.yaml"),
]


def _load_env_file():
    """Carrega variaveis de um .env sem precisar de source no zshrc."""
    for env_path in _ENV_SEARCH_PATHS:
        if os.path.isfile(env_path):
            with open(env_path, "r", encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if not line or line.startswith("#"):
                        continue
                    if line.startswith("export "):
                        line = line[7:]
                    if "=" not in line:
                        continue
                    key, _, value = line.partition("=")
                    key = key.strip()
                    value = value.strip().strip('"').strip("'")
                    if key and value and not os.environ.get(key):
                        os.environ[key] = value
            return env_path
    return None


def _find_yaml_path():
    """Encontra google-ads.yaml para fallback do SDK."""
    for yaml_path in _YAML_SEARCH_PATHS:
        if os.path.isfile(yaml_path):
            return yaml_path
    return None


def mask_token(token):
    """Mascara token pra nao vazar em logs/output. Mostra so os 6 primeiros chars."""
    if not token or len(token) < 10:
        return "***"
    return f"{token[:6]}...{token[-4:]}"


# ---------------------------------------------------------------------------
# Auth & SDK init
# ---------------------------------------------------------------------------

_client = None


def init_client():
    """Inicializa o GoogleAdsClient com .env ou google-ads.yaml."""
    global _client
    if _client is not None:
        return _client

    ensure_sdk()
    from google.ads.googleads.client import GoogleAdsClient

    # Tenta carregar do .env primeiro
    env_file = _load_env_file()

    dev_token = os.environ.get("GOOGLE_ADS_DEVELOPER_TOKEN")
    client_id = os.environ.get("GOOGLE_ADS_CLIENT_ID")
    client_secret = os.environ.get("GOOGLE_ADS_CLIENT_SECRET")
    refresh_token = os.environ.get("GOOGLE_ADS_REFRESH_TOKEN")
    login_customer_id = os.environ.get("GOOGLE_ADS_LOGIN_CUSTOMER_ID")

    if dev_token and client_id and client_secret and refresh_token:
        # Build from env vars
        config = {
            "developer_token": dev_token,
            "client_id": client_id,
            "client_secret": client_secret,
            "refresh_token": refresh_token,
            "use_proto_plus": True,
        }
        if login_customer_id:
            config["login_customer_id"] = login_customer_id.replace("-", "")

        _client = GoogleAdsClient.load_from_dict(config)
        source = env_file or "env vars"
        print(f"Client inicializado via {source} (token: {mask_token(dev_token)})", file=sys.stderr)
        return _client

    # Fallback: google-ads.yaml
    yaml_path = _find_yaml_path()
    if yaml_path:
        _client = GoogleAdsClient.load_from_storage(yaml_path)
        print(f"Client inicializado via {yaml_path}", file=sys.stderr)
        return _client

    print("ERRO: Credenciais Google Ads nao encontradas.", file=sys.stderr)
    print("  Crie o arquivo .claude/skills/google-ads/.env com:", file=sys.stderr)
    print('  GOOGLE_ADS_DEVELOPER_TOKEN="seu-token"', file=sys.stderr)
    print('  GOOGLE_ADS_CLIENT_ID="seu-client-id"', file=sys.stderr)
    print('  GOOGLE_ADS_CLIENT_SECRET="seu-secret"', file=sys.stderr)
    print('  GOOGLE_ADS_REFRESH_TOKEN="seu-refresh-token"', file=sys.stderr)
    print('  GOOGLE_ADS_LOGIN_CUSTOMER_ID="1234567890"', file=sys.stderr)
    print("", file=sys.stderr)
    print("  Ou crie um google-ads.yaml na mesma pasta.", file=sys.stderr)
    print("  Ou rode: /google-ads setup", file=sys.stderr)
    sys.exit(1)


def get_default_customer_id():
    """Retorna o customer ID padrao da env var GOOGLE_ADS_CUSTOMER_ID."""
    _load_env_file()
    customer_id = os.environ.get("GOOGLE_ADS_CUSTOMER_ID")
    if not customer_id:
        print("ERRO: Nenhuma conta informada.", file=sys.stderr)
        print("  Use --customer-id 1234567890 ou defina GOOGLE_ADS_CUSTOMER_ID.", file=sys.stderr)
        sys.exit(1)
    return customer_id.replace("-", "")


def resolve_customer_id(args_customer_id=None):
    """Resolve customer ID: argumento CLI > env var."""
    if args_customer_id:
        return args_customer_id.replace("-", "")
    return get_default_customer_id()


# ---------------------------------------------------------------------------
# GAQL query runner
# ---------------------------------------------------------------------------

def run_query(customer_id, query):
    """Executa uma query GAQL e retorna lista de rows como dicts."""
    client = init_client()
    service = client.get_service("GoogleAdsService")

    results = []
    try:
        response = service.search(customer_id=customer_id, query=query)
        for row in response:
            results.append(_row_to_dict(row))
    except Exception as e:
        handle_google_error(e)

    return results


def _row_to_dict(row):
    """Converte uma row protobuf para dict legivel."""
    from google.protobuf.json_format import MessageToDict
    return MessageToDict(row._pb, preserving_proto_field_name=True)


# ---------------------------------------------------------------------------
# Cost conversion
# ---------------------------------------------------------------------------

def micros_to_currency(micros):
    """Converte cost_micros para valor monetario (/ 1_000_000)."""
    if micros is None:
        return 0.0
    try:
        return int(micros) / 1_000_000
    except (ValueError, TypeError):
        return 0.0


def format_cost(micros):
    """Formata cost_micros como string com 2 casas decimais."""
    return f"{micros_to_currency(micros):.2f}"


def convert_costs_in_row(row):
    """Converte todos os campos cost_micros de uma row para reais."""
    if not isinstance(row, dict):
        return row
    for key, value in list(row.items()):
        if isinstance(value, dict):
            convert_costs_in_row(value)
        elif key.endswith("_micros") or key == "amount_micros":
            row[key] = micros_to_currency(value)
            # Add a friendly key without _micros suffix
            friendly_key = key.replace("_micros", "")
            if friendly_key not in row:
                row[friendly_key] = row[key]
    return row


# ---------------------------------------------------------------------------
# Output helpers
# ---------------------------------------------------------------------------

def print_json(obj):
    """Serializa e printa qualquer objeto para stdout."""
    if isinstance(obj, list):
        obj = [convert_costs_in_row(row) for row in obj]
    elif isinstance(obj, dict):
        obj = convert_costs_in_row(obj)
    print(json.dumps(obj, indent=2, ensure_ascii=False, default=str))


def print_error(msg):
    """Printa erro formatado para stderr."""
    print(f"ERRO: {msg}", file=sys.stderr)


# ---------------------------------------------------------------------------
# Error handling
# ---------------------------------------------------------------------------

def handle_google_error(error):
    """Trata erros do Google Ads API e exibe mensagem util."""
    ensure_sdk()
    from google.ads.googleads.errors import GoogleAdsException

    if isinstance(error, GoogleAdsException):
        error_data = {
            "error": True,
            "message": str(error),
            "errors": [],
        }
        for ga_error in error.failure.errors:
            err = {
                "error_code": str(ga_error.error_code),
                "message": ga_error.message,
            }
            if ga_error.location:
                err["field_path"] = str(ga_error.location)
            error_data["errors"].append(err)

        # Rate limiting
        if "RESOURCE_EXHAUSTED" in str(error):
            error_data["hint"] = "Rate limit atingido. Aguarde alguns minutos antes de tentar novamente."

        # Auth errors
        if "AUTHENTICATION_ERROR" in str(error) or "AUTHORIZATION_ERROR" in str(error):
            error_data["hint"] = "Erro de autenticacao. Verifique developer_token, refresh_token e permissoes."

        # Permission
        if "PERMISSION_DENIED" in str(error):
            error_data["hint"] = "Sem permissao. Verifique se o login_customer_id (MCC) tem acesso a esta conta."

        print(json.dumps(error_data, indent=2, ensure_ascii=False, default=str))
        sys.exit(1)
    else:
        print_error(str(error))
        sys.exit(1)


def handle_google_error_decorator(func):
    """Decorator que trata erros do Google Ads API."""
    def wrapper(*args, **kwargs):
        ensure_sdk()
        from google.ads.googleads.errors import GoogleAdsException
        try:
            return func(*args, **kwargs)
        except GoogleAdsException as e:
            handle_google_error(e)
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

def add_customer_arg(parser, required=False):
    """Adiciona argumento --customer-id ao parser."""
    parser.add_argument(
        "--customer-id",
        required=required,
        help="Google Ads customer ID (sem hifens). Padrao: GOOGLE_ADS_CUSTOMER_ID"
    )


def add_date_args(parser):
    """Adiciona argumentos de data ao parser."""
    parser.add_argument(
        "--date-range",
        default="LAST_30_DAYS",
        help="Periodo: LAST_7_DAYS, LAST_14_DAYS, LAST_30_DAYS, THIS_MONTH, LAST_MONTH, etc (default: LAST_30_DAYS)"
    )
    parser.add_argument("--since", help="Data inicio (YYYY-MM-DD)")
    parser.add_argument("--until", help="Data fim (YYYY-MM-DD)")


def add_limit_arg(parser, default=None):
    """Adiciona argumento --limit ao parser."""
    parser.add_argument("--limit", type=int, default=default, help="Limite de resultados")


def add_campaign_filter(parser):
    """Adiciona argumento --campaign-id ao parser."""
    parser.add_argument("--campaign-id", help="Filtrar por campaign ID")


def build_date_clause(args):
    """Constroi clausula WHERE de data a partir dos argumentos."""
    if hasattr(args, "since") and args.since and hasattr(args, "until") and args.until:
        return f"segments.date BETWEEN '{args.since}' AND '{args.until}'"
    # Map friendly names to GAQL date ranges
    date_range = getattr(args, "date_range", "LAST_30_DAYS")
    return f"segments.date DURING {date_range}"


def parse_json_arg(json_str, arg_name="argumento"):
    """Faz parse de um argumento JSON string."""
    if not json_str:
        return None
    try:
        return json.loads(json_str)
    except json.JSONDecodeError as e:
        print_error(f"JSON invalido no argumento {arg_name}: {e}")
        sys.exit(1)
