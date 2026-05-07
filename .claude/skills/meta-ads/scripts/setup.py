#!/usr/bin/env python3
"""
Meta Ads ClaudePRO - Install Wizard
Verifica dependencias, token e conectividade com a API.

Uso: python3 setup.py
"""

import os
import sys
import shutil


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
        print("  [FALHOU] META_ADS_TOKEN nao definida")
        print("           Adicione ao ~/.zshrc ou ~/.bashrc:")
        print('           export META_ADS_TOKEN="seu-token-aqui"')
        return False
    masked = token[:10] + "..." + token[-5:]
    print(f"  [OK] META_ADS_TOKEN definida ({masked})")
    return True


def check_account():
    account = os.environ.get("META_AD_ACCOUNT_ID")
    if not account:
        print("  [AVISO] META_AD_ACCOUNT_ID nao definida (opcional)")
        print("          Voce pode definir uma conta padrao:")
        print('          export META_AD_ACCOUNT_ID="act_123456789"')
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

    print("\n2. Autenticacao:")
    token_ok = check_token()
    account_ok = check_account()

    print("\n3. Conectividade:")
    if sdk_ok and token_ok:
        api_ok = check_api_connection()
        if api_ok:
            check_ad_accounts()
    else:
        print("  [PULOU] Resolva dependencias e token primeiro")
        api_ok = False

    # Summary
    print("\n" + "=" * 55)
    all_ok = py_ok and sdk_ok and token_ok
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
