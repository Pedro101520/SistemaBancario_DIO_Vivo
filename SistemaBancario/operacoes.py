# from .extrato import *

from tkinter import messagebox

global clientes, saldo
saldo = 0
clientes = {}

def obter_cliente(cliente):
    global clientes
    clientes = cliente

def sacar(valor):
    global saldo
    print("Saldo no saque: ", saldo)
    saques = ""
    LIMITE = 500

    if valor > saldo:
        messagebox.showinfo("Aviso", "Não foi possível sacar por falta de saldo")
        print(saldo)
    elif valor <= LIMITE:
        saques = f"Saque de: R$ {valor:.2f}"
        # getOperacao(saques)
        saldo -= valor
        messagebox.showinfo("Aviso", "Operação Efetuada")
        # getSaldo(saldo)
    else:
        return messagebox.showinfo("Aviso", "Limite por saque é de 500")
    print(saldo)
    return saldo

def depositar(valor):
    global saldo 
    # depositos = ""
    # depositos = f"Depósito de: R$ {valor:.2f}" 
    # getOperacao(depositos)
    saldo += valor
    messagebox.showinfo("Aviso", "Operação Efetuada")
    # getSaldo(saldo)
    print(saldo)
    return saldo

def operacao(valor, operacao, cpf, conta):
    global saldo, clientes
    conta = int(conta)
    for cliente in clientes:
        if cpf == cliente["CPF"]:
            for numConta in cliente["Conta"]:
                if conta == numConta["numConta"]:
                    saldo = numConta["Saldo"]
                    if operacao == 1:
                        numConta["Depositos"] += f"Deposito de: R$ {valor:.2f}"
                        depositar(valor)
                    elif operacao == 2:
                        if numConta["qtdeSaques"] < 3:
                            numConta["Saques"] += f"Saque de: R$ {valor:.2f}"
                            sacar(valor)
                            numConta["qtdeSaques"] += 1
                        else:
                            messagebox.showinfo("Aviso", "Limite diário de saques atingido")
                    numConta["Saldo"] = saldo
                else:
                    print("CPF ou Conta inválidos")
    print(clientes)


def get_cliente():
    return clientes

