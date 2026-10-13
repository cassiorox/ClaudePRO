"""Setup guiado do meta-vv-publicos: valida o token na API, mostra suas contas
de anuncio e paginas (pra voce copiar os act_...).

O token NUNCA entra por argumento de linha de comando nem pelo chat do Claude
(ficaria gravado na transcricao e no historico do shell). Ele entra no .env pela
mao do dono:

  1. cp .env.example .env   (o proprio setup cria, se nao existir)
  2. abra o .env num editor e preencha META_TOKEN (e, opcional, META_INSIGHTS_TOKEN)
  3. python setup.py        valida o token do .env e lista contas e paginas

Rodando num terminal seu (fora do Claude), se o .env estiver vazio o setup pede o
token com entrada oculta e grava direto no .env.
"""
import getpass, json, os, shutil, stat, sys, urllib.error, urllib.parse, urllib.request

G = "https://graph.facebook.com/v21.0"
HERE = os.path.dirname(os.path.abspath(__file__))
ENV_PATH = os.path.join(HERE, ".env")
EXAMPLE_PATH = os.path.join(HERE, ".env.example")

PERMS_ADS = {"ads_management"}
PERMS_ORGANICO = {"pages_show_list", "pages_read_engagement", "instagram_basic", "instagram_manage_insights"}


def get(path, params, token):
    url = "%s/%s?%s" % (G, path, urllib.parse.urlencode(dict(params, access_token=token)))
    try:
        with urllib.request.urlopen(url, timeout=60) as r:
            return json.load(r)
    except urllib.error.HTTPError as e:
        try:
            return {"_error": json.loads(e.read()).get("error", {})}
        except Exception:
            return {"_error": {"message": str(e)}}
    except Exception as e:
        return {"_error": {"message": str(e)}}


def fail(msg):
    print("\nX %s" % msg)
    sys.exit(1)


def read_env():
    env = {}
    if os.path.exists(ENV_PATH):
        for line in open(ENV_PATH, encoding="utf-8"):
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                k, v = line.split("=", 1)
                env[k.strip()] = v.strip().strip('"')
    return env


def protect(path):
    try:
        os.chmod(path, stat.S_IRUSR | stat.S_IWUSR)  # 600: so o dono le
    except OSError:
        pass


def write_token(tok):
    """Grava META_TOKEN no .env preservando o resto do arquivo."""
    lines, done = [], False
    if os.path.exists(ENV_PATH):
        for line in open(ENV_PATH, encoding="utf-8").read().splitlines():
            if line.strip().startswith("META_TOKEN="):
                line, done = "META_TOKEN=%s" % tok, True
            lines.append(line)
    if not done:
        lines.append("META_TOKEN=%s" % tok)
    with open(ENV_PATH, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")
    protect(ENV_PATH)


def pedir_preenchimento():
    if not os.path.exists(ENV_PATH) and os.path.exists(EXAMPLE_PATH):
        shutil.copyfile(EXAMPLE_PATH, ENV_PATH)
        protect(ENV_PATH)
        print("\nok .env criado a partir do .env.example em %s" % ENV_PATH)
    print("\n>> Abra o arquivo abaixo num editor, preencha META_TOKEN e salve:")
    print("   %s" % ENV_PATH)
    print("   Depois rode de novo: python setup.py")
    print("   (nao cole o token no chat nem passe por argumento)")
    sys.exit(2)


def main():
    if len(sys.argv) > 1:
        fail("o setup nao aceita argumentos. O token vai no .env, preenchido por voce "
             "(veja o topo deste arquivo). Nunca passe o token na linha de comando.")

    print("")
    print("=== meta-vv-publicos: setup ===")
    if sys.version_info < (3, 9):
        fail("Python 3.9+ necessario (voce tem %d.%d)." % sys.version_info[:2])
    print("ok Python %d.%d" % sys.version_info[:2])

    env = read_env()
    tok = (os.environ.get("META_TOKEN") or env.get("META_TOKEN") or "").strip()
    gravar = False
    if not tok:
        if sys.stdin.isatty():
            # terminal do proprio usuario: entrada oculta, vai direto pro .env
            tok = getpass.getpass("\nCole seu token da Meta (nao aparece na tela) e aperte Enter: ").strip()
            gravar = bool(tok)
        if not tok:
            pedir_preenchimento()
    else:
        if os.path.exists(ENV_PATH):
            protect(ENV_PATH)
        print("ok META_TOKEN lido do .env")

    # 1. token valido?
    me = get("me", {"fields": "id,name"}, tok)
    if "_error" in me:
        fail("token recusado pela Meta: %s" % me["_error"].get("message", "?"))
    print("ok token valido (%s)" % me.get("name", me.get("id")))

    # 2. permissoes
    perms = get("me/permissions", {}, tok)
    granted = {p["permission"] for p in perms.get("data", []) if p.get("status") == "granted"}
    if granted:
        faltam_ads = PERMS_ADS - granted
        faltam_org = PERMS_ORGANICO - granted
        if faltam_ads:
            print("!! faltam permissoes pra CRIAR publicos: %s" % sorted(faltam_ads))
        else:
            print("ok permissoes de ads")
        if faltam_org:
            print("!! faltam pro modo ORGANICO (vv_publicos.py): %s" % sorted(faltam_org))
            print("   (o modo por campanha, vv_campanha.py, nao precisa delas)")
        else:
            print("ok permissoes de Instagram/paginas")
    else:
        print("!! nao consegui ler as permissoes (system user nao expoe) — seguindo")

    # 3. contas de anuncio
    accs = get("me/adaccounts", {"fields": "name", "limit": 50}, tok)
    if "_error" not in accs and accs.get("data"):
        print("\nSuas contas de anuncio (use no --contas):")
        for acc in accs["data"][:25]:
            print("  %-22s %s" % (acc["id"], acc.get("name", "")))
        primeira = accs["data"][0]["id"]
    else:
        print("\n!! nao consegui listar contas de anuncio (%s)" % err_txt(accs))
        primeira = "act_SEU_ID"

    # 4. paginas com IG (so relevante pro modo organico)
    pages = get("me/accounts", {"fields": "name,instagram_business_account", "limit": 50}, tok)
    if "_error" not in pages and pages.get("data"):
        com_ig = [p for p in pages["data"] if p.get("instagram_business_account")]
        print("\nPaginas com Instagram vinculado (modo organico):")
        for p in com_ig[:25]:
            print("  %s" % p["name"])
        if not com_ig:
            print("  (nenhuma — o modo organico nao vai achar videos)")
    else:
        print("\n!! nenhuma pagina visivel pro token (modo por campanha funciona mesmo assim)")

    # 5. grava o token no .env (so quando veio da entrada oculta)
    if gravar:
        if os.path.exists(EXAMPLE_PATH) and not os.path.exists(ENV_PATH):
            shutil.copyfile(EXAMPLE_PATH, ENV_PATH)
        write_token(tok)
        print("\nok token gravado em %s" % ENV_PATH)

    print("\nProximo passo (sempre com --dry-run primeiro):")
    print("  python vv_publicos.py --contas %s --retencoes 75,95 --min-views 100000 --dry-run" % primeira)
    print("  python vv_campanha.py --contas %s --campanha \"NOME DA CAMPANHA\" --dry-run" % primeira)
    print("")


def err_txt(res):
    return (res.get("_error", {}) or {}).get("message", "?")[:100]


if __name__ == "__main__":
    main()
