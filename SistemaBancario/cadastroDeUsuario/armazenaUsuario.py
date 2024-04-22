from .validaCPF import valida

from tkinter import messagebox

clientes = []

def armazena(nome, cpf, cep, cidade, estado, rua):
    if valida(cpf):
        cliente = {"Nome": nome, "CPF": cpf, "CEP": cep, "Cidade": cidade, "Estado": estado, "Rua": rua}

    count = 0
    for c in clientes:
        if c["CPF"] == cpf:
            count += 1
    if count >= 1:
        messagebox.showerror("Atenção", "CPF já cadastrado")
    else:
        clientes.append(cliente)
    
    
    for i in clientes:
        print(i)
