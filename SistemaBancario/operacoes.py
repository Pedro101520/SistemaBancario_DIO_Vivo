from .extrato import *

from tkinter import messagebox

global clientes, saldo
saldo = 0
clientes = {}
qtdeSaques = 0

def obter_cliente(cliente):
    global clientes
    clientes = cliente

# def vincular_cliente(cpf):
#     global saldo
#     if cpf == clientes["CPF"]:
#         conta = clientes["Conta"]
#         saldo = conta[0]["Saldo"]
#         print("Cliente com Saldo: ", clientes)
        # saldo = novo_saldo
        


def sacar(valor):
    global saldo, qtdeSaques
    print("Saldo no saque: ", saldo)
    saques = ""
    LIMITE = 500

    if valor > saldo:
        messagebox.showinfo("Aviso", "Não foi possível sacar por falta de saldo")
        print(saldo)
    elif valor <= LIMITE:
        if qtdeSaques < 3:
            saques = f"Saque de: R$ {valor:.2f}"
            getOperacao(saques)
            saldo -= valor
            messagebox.showinfo("Aviso", "Operação Efetuada")
            getSaldo(saldo)
            qtdeSaques += 1
        else:
            messagebox.showinfo("Aviso", "Limite diário de saques atingida")
    else:
        messagebox.showinfo("Aviso", "Limite por saque é de 500")
    print(saldo)
    return saldo

def depositar(valor):
    global saldo 
    depositos = ""
    depositos = f"Depósito de: R$ {valor:.2f}" 
    getOperacao(depositos)
    saldo += valor
    messagebox.showinfo("Aviso", "Operação Efetuada")
    getSaldo(saldo)
    print(saldo)
    return saldo

def operacao(valor, operacao, cpf, conta):
    global saldo
    for i in clientes["CPF"]:
        if i == cpf:
            print("Teste CPF", i)
            saldo = clientes["Conta"][i]["Saldo"]
            if operacao == 1:
                depositar(valor)
            elif operacao == 2:
                sacar(valor)
        clientes["Conta"][i]["Saldo"] = saldo
    print("Saldo na função operações: ", clientes)