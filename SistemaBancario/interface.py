from .operacoes import *

from tkinter import *
from tkinter import messagebox

def is_float(valor):
    try:
        float(valor)
        return True
    except:
        return False

def botaoNoticia(valor, app, opcao, txtQtde):
    if not is_float(valor):
        messagebox.showerror("Atenção", "Digite apenas numeros")
    else:
        valor = float(valor)
        if valor < 1:
            messagebox.showerror("Atenção", "Apenas numeros positivos")
        else:
            messagebox.showinfo("Aviso", "Operação Efetuada")
            operacao(valor, app, opcao)
            txtQtde.delete(0, END)

def window():
    app = Tk()
    app.title("Sistema Bancário")
    app.geometry("500x300")
    app.configure(background='#dde')
    Label(
        app,
        text = "Digite o valor: ",
        background = "#dde",
        foreground = "#009",
        anchor = W
    ).place(x=10, y=10, width=200, height=20)
    txtQtde=Entry(app)
    txtQtde.place(x=225, y=10, width=50, height=20)

    opcao = IntVar()

    lbl_aviso = Label(app, text="Selecione uma opção", background="#dde")
    lbl_aviso.place(x=15, y=70)

    rb_deposito = Radiobutton(app, text="Deposito", value=1, variable=opcao, background="#dde")
    rb_deposito.place(x=15, y=100)
    rb_saque = Radiobutton(app, text="Saque", value=2, variable=opcao, background="#dde")
    rb_saque.place(x=15, y=130)
    rb_extrato = Radiobutton(app, text="Extrato", value=3, variable=opcao, background="#dde")
    rb_extrato.place(x=15, y=160)

    Button(app, text="Confirma", command=lambda: botaoNoticia(txtQtde.get(), app, opcao.get(), txtQtde)).place(x=10, y=270, width=100, height=20)
    app.mainloop()