#!/usr/bin/env python3
"""Gera o arquivo de credenciais (ADC) que o servidor MCP do Google Ads espera.

O google-ads-mcp autentica via Application Default Credentials, e nao pelas
variaveis GOOGLE_ADS_CLIENT_ID / CLIENT_SECRET / REFRESH_TOKEN. Este script le
essas tres variaveis do .env da skill google-ads e escreve um adc.json no
formato "authorized_user", que e o que a biblioteca google.auth entende.

Uso:
    python3 .claude/skills/google-ads/mcp/criar-adc.py
"""

import json
import os
from pathlib import Path

PASTA = Path(__file__).resolve().parent
SKILL = PASTA.parent
SAIDA = PASTA / "adc.json"

# Procura o .env na pasta da skill primeiro; depois na raiz do workspace.
CANDIDATOS = (
    SKILL / ".env",
    SKILL.parents[2] / ".env",
)

OBRIGATORIAS = (
    "GOOGLE_ADS_CLIENT_ID",
    "GOOGLE_ADS_CLIENT_SECRET",
    "GOOGLE_ADS_REFRESH_TOKEN",
)


def ler_env(caminho: Path) -> dict:
    valores = {}
    for linha in caminho.read_text(encoding="utf-8").splitlines():
        linha = linha.strip()
        if not linha or linha.startswith("#") or "=" not in linha:
            continue
        chave, _, valor = linha.partition("=")
        valores[chave.strip()] = valor.strip().strip('"').strip("'")
    return valores


def main() -> None:
    env_path = next((c for c in CANDIDATOS if c.exists()), None)
    if env_path is None:
        procurados = "\n  ".join(str(c) for c in CANDIDATOS)
        raise SystemExit(f"Nao achei nenhum .env. Procurei em:\n  {procurados}")

    env = ler_env(env_path)
    faltando = [c for c in OBRIGATORIAS if not env.get(c)]
    if faltando:
        raise SystemExit(
            f"Faltam no {env_path}: " + ", ".join(faltando) +
            "\nRode antes: python3 .claude/skills/google-ads/scripts/setup.py full"
        )

    adc = {
        "type": "authorized_user",
        "client_id": env["GOOGLE_ADS_CLIENT_ID"],
        "client_secret": env["GOOGLE_ADS_CLIENT_SECRET"],
        "refresh_token": env["GOOGLE_ADS_REFRESH_TOKEN"],
    }

    SAIDA.write_text(json.dumps(adc, indent=2) + "\n", encoding="utf-8")
    os.chmod(SAIDA, 0o600)
    print(f"OK: {SAIDA}  (lido de {env_path})")
    print("Login customer id:", env.get("GOOGLE_ADS_LOGIN_CUSTOMER_ID") or "(nao definido, so precisa com MCC)")


if __name__ == "__main__":
    main()
