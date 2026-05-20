# Clientes

Cada cliente tem sua própria pasta aqui dentro, e cada pasta tem (no mínimo) um `contexto.md`.

```
clientes/
  _template/
    contexto.md      ← modelo, não é um cliente real
  nome-do-cliente/
    contexto.md      ← contexto daquele cliente
  outro-cliente/
    contexto.md
```

## Como adicionar um cliente

Diga **`novo cliente`** e a skill cuida do resto: pede o contexto, cria a pasta e salva o `contexto.md`.

## Por que isso importa

Quando você pedir pra criar algo pra um cliente (criativo, campanha, proposta, copy),
o Claude lê o `contexto.md` daquele cliente primeiro pra calibrar tudo ao negócio dele.

Recomendado que **todo cliente tenha um `contexto.md`**. Se faltar, o Claude vai sugerir rodar `novo cliente`.
