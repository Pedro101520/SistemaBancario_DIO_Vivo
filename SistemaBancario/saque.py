from tkinter import messagebox

from .deposito import *

def saque(valor, app):
    SAQUES = 3
    LIMITE = 500

    if valor < depositar():
        messagebox.showinfo("Aviso", "Não foi possível sacar por falta de saldo")
