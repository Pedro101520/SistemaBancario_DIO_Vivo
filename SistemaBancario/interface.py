from .operacoes import *
from .extrato import *
from .cadastroDeUsuario.cadUsuario import *
from .criacaoDeConta.criaConta import *
from .criacaoDeConta.listarContas import windowCliente
from tkinter import *
from tkinter import messagebox

def is_float(valor):
    try:
        float(valor)
        return True
    except:
        return False

def botaoBanco(valor, opcao, txtQtde, cpf, conta):
    if opcao == 3:
        windowCad()
    elif opcao == 4:
        windowConta()
    elif opcao == 5:
        windowCliente()
    elif not is_float(valor):
        messagebox.showerror("Atenção", "Digite apenas numeros")
    else:
        valor = float(valor)
        if valor < 0:
            messagebox.showerror("Atenção", "Apenas numeros positivos")
        else:
            operacao(valor, opcao, cpf, conta)
            txtQtde.delete(0, END)
    
def botaoExtrato(conta, cpf):
    # try:
    geraPdf(conta, cpf)
    # except PermissionError:
    #     messagebox.showerror("Atenção", "Feche o extrato aberto, e tente novamente")

def botaoSair(app): app.destroy()

def window():
    app = Tk()
    app.title("Sistema Bancário")
    app.geometry("500x300")
    app.configure(background='#dde')
    Label(
        app,
        text = "Digite o valor: ",
        background = "#dde",
        foreground = "#000",
        anchor = W
    ).place(x=10, y=10, width=200, height=20)
    txtQtde=Entry(app)
    txtQtde.place(x=100, y=10, width=50, height=20)
    Label(
        app,
        text = "Digite o CPF do titular da conta: ",
        background = "#dde",
        foreground = "#000",
        anchor = W
    ).place(x=170, y=10, width=200, height=20)
    txtCPF=Entry(app)
    txtCPF.place(x=350, y=10, width=50, height=20)
    Label(
        app,
        text = "Informe uma conta: ",
        background = "#dde",
        foreground = "#000",
        anchor = W
    ).place(x=10, y=40, width=200, height=20)
    txtConta=Entry(app)
    txtConta.place(x=130, y=40, width=50, height=20)

    opcao = IntVar()

    lbl_aviso = Label(app, text="Selecione uma opção", background="#dde")
    lbl_aviso.place(x=15, y=70)

    rb_deposito = Radiobutton(app, text="Deposito", value=1, variable=opcao, background="#dde")
    rb_deposito.place(x=15, y=100)
    rb_saque = Radiobutton(app, text="Saque", value=2, variable=opcao, background="#dde")
    rb_saque.place(x=15, y=130)
    rb_novoUsuario = Radiobutton(app, text="Cadastrar Usuário", value=3, variable=opcao, background="#dde")
    rb_novoUsuario.place(x=15, y=160)
    rb_criaconta = Radiobutton(app, text="Criar Conta", value=4, variable=opcao, background="#dde")
    rb_criaconta.place(x=15, y=190)
    rb_listarConta = Radiobutton(app, text="Listar Contas", value=5, variable=opcao, background="#dde")
    rb_listarConta.place(x=15, y=220)

    Button(app, text="Confirma", command=lambda: botaoBanco(txtQtde.get().replace(',', '.'), opcao.get(), txtQtde, txtCPF.get(), txtConta.get())).place(x=10, y=270, width=100, height=20)
    Button(app, text="Gerar Extrato", command=lambda: botaoExtrato(txtConta.get(), txtCPF.get())).place(x=130, y=270, width=100, height=20)
    Button(app, text="Sair", command=lambda: botaoSair(app)).place(x=250, y=270, width=100, height=20)
    app.mainloop()