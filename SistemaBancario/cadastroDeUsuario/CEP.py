import requests
from tkinter import messagebox

def acessaCEP(cep):
    link = f'https://viacep.com.br/ws/{cep}/json/'
    requisicao = requests.get(link)
    if requisicao.status_code == 200:
        dic_requisicao = requisicao.json()
        uf = dic_requisicao['uf']
        cidade = dic_requisicao['localidade']
        rua = dic_requisicao['logradouro']
    else:
        messagebox.showinfo("Atenção", "Verifique o CEP, e tente novamente")

    print(uf)
    print(cidade)
    print(rua)