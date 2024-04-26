from tkinter import *

from .validaConta import *

def windowConta():
    app = Tk()
    app.title("Criação de Conta")
    app.geometry("500x300")
    app.configure(background='#dde')

    Label(
        app,
        text = "Informe seu CPF: ",
        background = "#dde",
        foreground = "#000",
        anchor = W
    ).place(x=10, y=10, width=200, height=20)
    txtCPF=Entry(app)
    txtCPF.place(x=140, y=10, width=170, height=20)

    Button(app, text="Criar Conta", command=lambda: criaConta(txtCPF.get(), app)).place(x=10, y=270, width=100, height=20)
    app.mainloop()