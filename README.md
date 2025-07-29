# Contrato SaaS – MVP

API em FastAPI para geração de contratos simples com IA (GPT-4).

## Como usar localmente

1. Crie um `.env` com sua chave da OpenAI:

```
OPENAI_API_KEY=sk-...
```

2. Instale os requisitos:
```
pip install -r requirements.txt
```

3. Rode a API local:
```
uvicorn main:app --reload
```

## Deploy no Railway

1. Crie um repositório no GitHub com esses arquivos.
2. Vá até https://railway.app e clique em "New Project > Deploy from GitHub".
3. Adicione a variável de ambiente `OPENAI_API_KEY`.
4. Acesse a rota POST `/generate_contract` após deploy.

Pronto!