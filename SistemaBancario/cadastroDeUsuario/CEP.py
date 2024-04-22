import requests
from tkinter import messagebox

global uf, localidade, logradouro
uf = ""
localidade = ""
logradouro = ""

def acessaCEP(cep):
    global uf, localidade, logradouro
    link = f'https://viacep.com.br/ws/{cep}/json/'
    requisicao = requests.get(link)
    if requisicao.status_code == 200:
        dic_requisicao = requisicao.json()
        uf = dic_requisicao['uf']
        localidade = dic_requisicao['localidade']
        logradouro = dic_requisicao['logradouro']
    else:
        messagebox.showinfo("Atenção", "Verifique o CEP, e tente novamente")

def estado():
    global uf
    return uf

def cidade():
    global localidade
    return localidade

def rua():
    global logradouro
    return logradouro