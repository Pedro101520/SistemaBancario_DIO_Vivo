from tkinter import messagebox

saldo = 0
saques = 0

def sacar(valor):
    global saldo, saques
    LIMITE = 500

    if valor > saldo:
        messagebox.showinfo("Aviso", "Não foi possível sacar por falta de saldo")
        print(saldo)
    elif valor <= LIMITE:
        if saques < 3:
            saldo -= valor
            messagebox.showinfo("Aviso", "Operação Efetuada")
            saques += 1
        else:
            messagebox.showinfo("Aviso", "Limite diário de saques atingida")
    else:
        messagebox.showinfo("Aviso", "Limite por saque é de 500")
    return saldo

def depositar(valor):
    global saldo
    saldo += valor
    print(saldo)
    messagebox.showinfo("Aviso", "Operação Efetuada")
    return saldo

def operacao(valor, operacao):
    if operacao == 1:
        depositar(valor)
    elif operacao == 2:
        sacar(valor)

