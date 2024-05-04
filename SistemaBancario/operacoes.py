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
    LIMITE = 500

    if valor > saldo:
        messagebox.showinfo("Aviso", "Não foi possível sacar por falta de saldo")
        print(saldo)
    elif valor == 0:
        messagebox.showinfo("Aviso", "Não é possivel sacar igual a 0")
    elif valor <= LIMITE:
        saldo -= valor
        messagebox.showinfo("Aviso", "Operação Efetuada")
    else:
        return messagebox.showinfo("Aviso", "Limite por saque é de 500")
    print(saldo)
    return saldo

def depositar(valor):
    global saldo 
    if valor == 0:
        messagebox.showinfo("Aviso", "Não é possivel depositar valor igual a 0")
    saldo += valor
    messagebox.showinfo("Aviso", "Operação Efetuada")
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
                        if not numConta["Depositos"]:
                            numConta["Depositos"] = []
                        numConta["Depositos"].append(f"Deposito de: R$ {valor:.2f}")
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
                    messagebox.showinfo("Aviso", "Conta não encontrada. Verifique o CPF do usuário e tente novamente")
        else:          
            messagebox.showinfo("Aviso", "CPF não encontrado. Verifique o cadastro e a conta e tente novamente")
    print(clientes)


def get_cliente():
    return clientes

