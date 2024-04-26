from tkinter import *

from .CEP import *
from .armazenaUsuario import armazena
from .dataNascimento import *

def consultaCEP(event, txtEstado, txtCidade, txtRua):
    cep = event.widget.get()
    cep = cep.replace('.', '').replace('-', '').replace(' ', '')
    try:
        if len(cep) == 8:
            acessaCEP(cep)
            txtEstado.delete(0, END)
            txtEstado.insert(0, estado())
            txtCidade.delete(0, END)
            txtCidade.insert(0, cidade())
            txtRua.delete(0, END)
            txtRua.insert(0, rua())
    except:
        return

def ola(event):
    print("Ola")

def windowCad():
    app = Tk()
    app.title("Cadastro de Usuário")
    app.geometry("500x320")
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

    Label(
        app,
        text = "CEP: ",
        background = "#dde",
        foreground = "#000",
        anchor = W
    ).place(x=10, y=90, width=200, height=20)
    txtCEP=Entry(app)
    txtCEP.bind("<KeyRelease>", lambda event: consultaCEP(event, txtEstado, txtCidade, txtRua))
    txtCEP.place(x=70, y=90, width=170, height=20)

    Label(
        app,
        text = "Cidade: ",
        background = "#dde",
        foreground = "#000",
        anchor = W
    ).place(x=10, y=130, width=200, height=20)
    txtCidade=Entry(app)
    txtCidade.place(x=70, y=130, width=170, height=20)

    Label(
        app,
        text = "Estado: ",
        background = "#dde",
        foreground = "#000",
        anchor = W
    ).place(x=10, y=170, width=200, height=20)
    txtEstado=Entry(app)
    txtEstado.place(x=70, y=170, width=170, height=20)

    Label(
        app,
        text = "Rua: ",
        background = "#dde",
        foreground = "#000",
        anchor = W
    ).place(x=10, y=210, width=200, height=20)
    txtRua=Entry(app)
    txtRua.place(x=70, y=210, width=170, height=20)

    Label(
        app,
        text = "Data Nasc: ",
        background = "#dde",
        foreground = "#000",
        anchor = W
    ).place(x=10, y=250, width=200, height=20)
    txtData=Entry(app)
    txtData.bind("<Key>", lambda event: block_entry(event))
    txtData.bind("<Button-1>", lambda event: pick_date(event, txtData))
    txtData.place(x=70, y=250, width=170, height=20)

    Button(app, text="Cadastrar", command=lambda: armazena(txtNome.get(), txtCPF.get().replace('.', '').replace('-', ''), txtCEP.get(), txtCidade.get(), txtEstado.get(), txtRua.get(), app, txtData.get())).place(x=10, y=290, width=100, height=20)
    app.mainloop()