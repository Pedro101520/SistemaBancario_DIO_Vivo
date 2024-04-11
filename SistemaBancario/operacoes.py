from .deposito import *
from .saque import *

def operacao(valor, app, operacao):
    if operacao == 1:
        print(depositar(valor))
    elif operacao == 2:
        print(saque(valor, app))
