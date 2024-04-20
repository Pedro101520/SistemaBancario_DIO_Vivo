from tkinter import *

from .validaCPF import valida

def windowCad():
    app = Tk()
    app.title("Cadastro de Usuário")
    app.geometry("500x300")
    app.configure(background='#dde')

    Label(
        app,
        text = "Nome: ",
        background = "#dde",
        foreground = "#000",
        anchor = W
    ).place(x=10, y=10, width=200, height=20)
    txtNome=Entry(app)
    txtNome.place(x=70, y=10, width=170, height=20)

    Label(
        app,
        text = "CPF: ",
        background = "#dde",
        foreground = "#000",
        anchor = W
    ).place(x=10, y=50, width=200, height=20)
    txtCPF=Entry(app)
    txtCPF.place(x=70, y=50, width=170, height=20)

    Button(app, text="Cadastrar", command=lambda: valida(txtCPF.get().replace('.', '').replace('-', ''))).place(x=10, y=270, width=100, height=20)
    app.mainloop()