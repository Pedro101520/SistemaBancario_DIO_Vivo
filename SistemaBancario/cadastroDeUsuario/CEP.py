import requests

global uf, localidade, logradouro
uf = ""
localidade = ""
logradouro = ""

def isNumber(cep):
    try:
        for i in cep:
            int(i)
        return True
    except:
        return False

def acessaCEP(cep):
    global uf, localidade, logradouro
    link = f'https://viacep.com.br/ws/{cep}/json/'
    requisicao = requests.get(link)
    try:
        if requisicao.status_code == 200 and isNumber(cep):
            dic_requisicao = requisicao.json()
            uf = dic_requisicao['uf']
            localidade = dic_requisicao['localidade']
            logradouro = dic_requisicao['logradouro']
            return True
    except:
        return False

def estado():
    global uf
    return uf

def cidade():
    global localidade
    return localidade

def rua():
    global logradouro
    return logradouro