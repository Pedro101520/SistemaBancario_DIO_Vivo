from .extrato import *
from tkinter import messagebox

class Operacoes:

    def __init__(self) -> None:
        self.__saldo = 0
        self.__qtdeSaques = 0

    def sacar(self, valor):
        saques = ""
        LIMITE = 500

        if valor > self.__saldo:
            messagebox.showinfo("Aviso", "Não foi possível sacar por falta de saldo")
        elif valor <= LIMITE:
            if self.__qtdeSaques < 3:
                saques = f"Saque de: R$ {valor:.2f}"
                getOperacao(saques)
                self.__saldo -= valor
                messagebox.showinfo("Aviso", "Operação Efetuada")
                getSaldo(self.__saldo)
                self.__qtdeSaques += 1
            else:
                messagebox.showinfo("Aviso", "Limite diário de saques atingida")
        else:
            messagebox.showinfo("Aviso", "Limite por saque é de 500")

    def depositar(self, valor):
        depositos = ""
        depositos = f"Depósito de: R$ {valor:.2f}" 
        getOperacao(depositos)
        self.__saldo += valor
        messagebox.showinfo("Aviso", "Operação Efetuada")
        getSaldo(self.__saldo)

    def operacao(self, valor, operacao):
        if operacao == 1:
            self.depositar(valor)
        elif operacao == 2:
            self.sacar(valor)