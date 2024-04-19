from .extrato import *

from tkinter import messagebox

saldo = 0
qtdeSaques = 0

def sacar(valor):
    global saldo, qtdeSaques
    saques = ""
    LIMITE = 500

    if valor > saldo:
        messagebox.showinfo("Aviso", "Não foi possível sacar por falta de saldo")
        print(saldo)
    elif valor <= LIMITE:
        if qtdeSaques < 3:
            saques = f"Saque de: R$ {valor:.0f}"
            getOperacao(saques)
            saldo -= valor
            messagebox.showinfo("Aviso", "Operação Efetuada")
            getSaldo(saldo)
            qtdeSaques += 1
        else:
            messagebox.showinfo("Aviso", "Limite diário de saques atingida")
    else:
        messagebox.showinfo("Aviso", "Limite por saque é de 500")
    return saldo

def depositar(valor):
    global saldo 
    depositos = ""
    depositos = f"Depósito de: R$ {valor:.0f}" 
    getOperacao(depositos)
    saldo += valor
    messagebox.showinfo("Aviso", "Operação Efetuada")
    getSaldo(saldo)
    return saldo

def operacao(valor, operacao):
    if operacao == 1:
        depositar(valor)
    elif operacao == 2:
        sacar(valor)