
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.templating import Jinja2Templates
from weasyprint import HTML
from uuid import uuid4
import os

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/novo", response_class=HTMLResponse)
async def novo_contrato(request: Request):
    return templates.TemplateResponse("formulario.html", {"request": request})

@app.post("/gerar", response_class=HTMLResponse)
async def gerar_contrato(
    request: Request,
    nome: str = Form(...),
    servico: str = Form(...),
    valor: str = Form(...),
    data_servico: str = Form(...)
):
    html_content = templates.get_template("modelo.html").render({
        "nome": nome,
        "servico": servico,
        "valor": valor,
        "data_servico": data_servico
    })
    filename = f"contrato_{uuid4().hex}.pdf"
    output_path = os.path.join("pdfs", filename)
    os.makedirs("pdfs", exist_ok=True)
    HTML(string=html_content).write_pdf(output_path)
    return templates.TemplateResponse("sucesso.html", {"request": request, "pdf_url": f"/download/{filename}"})

@app.get("/download/{filename}", response_class=FileResponse)
async def download_pdf(filename: str):
    return FileResponse(path=f"pdfs/{filename}", media_type="application/pdf", filename=filename)
