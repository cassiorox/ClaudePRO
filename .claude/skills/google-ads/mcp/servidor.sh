#!/usr/bin/env bash
# Launcher do servidor MCP local do Google Ads.
# Le as credenciais do .env da skill google-ads e sobe o google-ads-mcp por
# stdio. Nenhum token fica escrito na configuracao do Claude Code.
set -euo pipefail

PASTA="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SKILL="$(dirname "$PASTA")"
RAIZ="$(cd "$SKILL/../../.." && pwd)"

ENV_FILE=""
for candidato in "$SKILL/.env" "$RAIZ/.env"; do
  if [ -f "$candidato" ]; then ENV_FILE="$candidato"; break; fi
done

if [ -z "$ENV_FILE" ]; then
  echo "Nao achei o .env. Esperado em $SKILL/.env" >&2
  exit 1
fi

# Exporta so as variaveis GOOGLE_ADS_* do .env, sem executar o resto do arquivo.
eval "$(python3 - "$ENV_FILE" <<'PY'
import pathlib, shlex, sys
for linha in pathlib.Path(sys.argv[1]).read_text(encoding="utf-8").splitlines():
    linha = linha.strip()
    if linha.startswith("GOOGLE_ADS_") and "=" in linha:
        chave, _, valor = linha.partition("=")
        valor = valor.strip().strip('"').strip("'")
        if valor:
            print(f"export {chave.strip()}={shlex.quote(valor)}")
PY
)"

# O google-ads-mcp autentica por Application Default Credentials.
export GOOGLE_APPLICATION_CREDENTIALS="$PASTA/adc.json"

if [ ! -f "$GOOGLE_APPLICATION_CREDENTIALS" ]; then
  echo "adc.json nao existe. Rode: python3 $PASTA/criar-adc.py" >&2
  exit 1
fi

exec "$HOME/.local/bin/google-ads-mcp" "$@"
