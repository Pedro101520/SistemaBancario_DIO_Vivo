from tkinter import messagebox

from .operacoes import get_cliente

from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, HRFlowable
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle

transferencias = ""

def geraPdf(conta, cpf):
    global transferencias
    operacoes = get_cliente()
    for operacao in operacoes:
        if cpf == operacao["CPF"]: 
            for numConta in operacao["Conta"]:
                if int(conta) == numConta["numConta"]:
                    saldoFinal = numConta["Saldo"]
                    transferencias = ""
                    for deposito in numConta["Depositos"]:
                        transferencias += str(deposito) + "<br></br>"
                    for saque in numConta["Saques"]:
                        transferencias += str(saque) + "<br></br>"

    if transferencias == "":
        messagebox.showinfo("Aviso", "Seu saldo é igual a R$ 0,00 pois não foram feitas movimentações")  
    else:
        pdf = SimpleDocTemplate("extrato.pdf", pagesize=letter)
        estilo_transacoes = ParagraphStyle(
            "transacoes",
            parent=getSampleStyleSheet()["Normal"],
            fontSize=10,
            textColor=colors.black
        )
        estilo_titulo = ParagraphStyle(
            "titulo",
            parent=getSampleStyleSheet()["Title"],
            fontSize=16,
            textColor=colors.black,
            alignment=1
        )
        titulo = "Extrato"
        paragrafos = [Paragraph(titulo, estilo_titulo)]
        paragrafos.append(Paragraph(transferencias, estilo_transacoes))
        paragrafos.append(HRFlowable(width="100%", thickness=1, lineCap='round', color=colors.black))
        paragrafos.append(Paragraph("Saldo Final: R${:.2f}".format(saldoFinal), estilo_transacoes))
        messagebox.showinfo("Aviso", "Extrato gerado, na pasta Sistema_Bancario")
        pdf.build(paragrafos)