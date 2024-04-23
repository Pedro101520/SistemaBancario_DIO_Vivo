from ..cadastroDeUsuario.armazenaUsuario import getCliente

def criaConta(cpf):
    dadosCliente = getCliente()
    for cliente in dadosCliente:
        if cpf == cliente["CPF"]:
            cliente["Agencia"] = "0001"
            cliente["Conta"] = 1
        else:
            print("Conta não encontrada")
    for cliente in dadosCliente:
        print(cliente)