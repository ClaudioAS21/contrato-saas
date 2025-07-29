from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import openai
import os

app = FastAPI()

openai.api_key = os.getenv("OPENAI_API_KEY")

class ContractRequest(BaseModel):
    nome_profissional: str
    cpf_profissional: str
    nome_cliente: str
    cpf_cliente: str
    descricao_servico: str
    valor: str
    data_inicio: str
    data_fim: str
    local: str
    plano: str

@app.post("/generate_contract")
def generate_contract(data: ContractRequest):
    if data.plano == "basico":
        pass

    prompt = f"""
Crie um contrato de prestação de serviços com linguagem simples e clara. Dados:

Profissional: {data.nome_profissional}, CPF: {data.cpf_profissional}
Cliente: {data.nome_cliente}, CPF: {data.cpf_cliente}
Serviço: {data.descricao_servico}
Valor: R$ {data.valor}
Período: de {data.data_inicio} até {data.data_fim}
Local do serviço: {data.local}

Escreva o contrato com clareza, tom respeitoso e com frases curtas. Não use termos jurídicos complexos.
"""

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "Você é um redator jurídico que cria contratos simples para autônomos."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.4,
            max_tokens=800
        )

        contrato = response['choices'][0]['message']['content']
        return {"contrato": contrato}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))