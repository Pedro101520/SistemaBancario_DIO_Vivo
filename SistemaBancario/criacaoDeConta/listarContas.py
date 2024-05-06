from tkinter import *
from tkinter import ttk
from ..cadastroDeUsuario.armazenaUsuario import getCliente

from tkinter import messagebox

def windowCliente():
    app = Tk()
    app.title("Lista de Contas")

    tree = ttk.Treeview(app, selectmode="browse", column=("column1", "column2", "column3"), show="headings")

    tree.column("column1", width=200, minwidth=50, stretch=NO)
    tree.heading("#1", text="Titular")

    tree.column("column2", width=200, minwidth=50, stretch=NO)
    tree.heading("#2", text="Agência")

    tree.column("column3", width=200, minwidth=50, stretch=NO)
    tree.heading("#3", text="Conta")

    scrollbar = ttk.Scrollbar(app, orient="vertical", command=tree.yview)
    tree.configure(yscroll=scrollbar.set)

    tree.grid(row=0, column=0)
    scrollbar.grid(row=0, column=1, sticky="ns")

    dados = getCliente()
    for cliente in dados:
        for conta in cliente["Conta"]:
            componente = [cliente["Nome"], conta["Agencia"], conta["numConta"]]
            tree.insert("", END, values=componente)

    app.mainloop()