from .validaCPF import valida

from tkinter import messagebox

clientes = []
def validaCEP(cep):
    for i in cep:
        try:
            int(i)
        except:
            messagebox.showerror("Atenção", "CEP inválido")
            return False
    return True
     

def armazena(nome, cpf, cep, cidade, estado, rua, app):

    if valida(cpf) and validaCEP(cep):
        cliente = {"Nome": nome, "CPF": cpf, "CEP": cep, "Cidade": cidade, "Estado": estado, "Rua": rua}
    else: return

    count = 0
    for c in clientes:
        if c["CPF"] == cpf:
            count += 1
    if count >= 1:
        messagebox.showerror("Atenção", "CPF já cadastrado")
    else:
        clientes.append(cliente)
    
    # for i in clientes:
    #     print(i)

    messagebox.showinfo("Atenção", "Cliente cadastrado") 
    app.destroy()

def getCliente():
    return clientes