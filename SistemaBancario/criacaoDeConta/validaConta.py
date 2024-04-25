from ..cadastroDeUsuario.armazenaUsuario import getCliente

from tkinter import messagebox

def criaConta(cpf):
    dadosCliente = getCliente()
    cliente_encontrado = False
    for cliente in dadosCliente:
        if cpf == cliente["CPF"]:
            cliente_encontrado = True
            if "Contas" not in cliente:
                cliente["Contas"] = []
            nova_conta = {"Agencia": "0001", "Numero": len(cliente["Contas"]) + 1}
            cliente["Contas"].append(nova_conta)
            print(cliente)
            break
    if not cliente_encontrado:
        messagebox.showinfo("Atenção", "Usuário não cadastrado")