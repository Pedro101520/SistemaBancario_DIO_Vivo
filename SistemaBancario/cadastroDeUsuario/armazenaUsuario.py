from .validaCPF import valida
from .CEP import acessaCEP

from tkinter import messagebox
import datetime

clientes = []
def validaCEP(cep):
    for i in cep:
        try:
            int(i)
        except:
            messagebox.showerror("Atenção", "CEP inválido")
            return False
    return True
     
def validaIdade(data):
    ano = int(data[6:])
    ano_atual = datetime.datetime.now().year
    if (ano_atual - ano) < 18:
        return False
    return True


def armazena(nome, cpf, cep, cidade, estado, rua, app, data):

    if not(validaIdade(data)):
        messagebox.showerror("Atenção", "Para realizar o cadastro é preciso ter no minímo 18 anos")
        return

    if not(acessaCEP(cep)):
        messagebox.showerror("Atenção", "CEP inválido")
        
    if valida(cpf) and acessaCEP(cep):
        cliente = {"Nome": nome, "CPF": cpf, "CEP": cep, "Cidade": cidade, "Estado": estado, "Rua": rua, "Data de nascimento": data}
    else: return

    count = 0
    for c in clientes:
        if c["CPF"] == cpf:
            count += 1
    if count >= 1:
        messagebox.showerror("Atenção", "CPF já cadastrado")
    else:
        clientes.append(cliente)

    messagebox.showinfo("Atenção", "Cliente cadastrado") 
    print(clientes)
    app.destroy()

def getCliente():
    return clientes