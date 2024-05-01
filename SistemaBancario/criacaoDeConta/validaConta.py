from ..cadastroDeUsuario.armazenaUsuario import getCliente
from ..operacoes import obter_cliente
from tkinter import messagebox

global qtdeConta
qtdeConta = 0

def criaConta(cpf, app):
    global qtdeConta
    
    dadosCliente = getCliente()
    cliente_encontrado = False
    
    for cliente in dadosCliente:
        if cpf == cliente["CPF"]:
            if "Conta" not in cliente:
                cliente["Conta"] = []
            qtdeConta += 1
            nova_conta = {"Agencia": "0001", "numConta": qtdeConta, "Saldo": 0}
            cliente["Conta"].append(nova_conta)
            print(cliente)
            obter_cliente(cliente)
            messagebox.showinfo("Sucesso", "Conta criada com sucesso")
            cliente_encontrado = True
            break

    if not cliente_encontrado:
        messagebox.showinfo("Atenção", "Usuário não cadastrado")

    app.destroy()
