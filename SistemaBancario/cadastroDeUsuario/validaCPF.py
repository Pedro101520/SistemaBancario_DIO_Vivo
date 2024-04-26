from tkinter import messagebox

def priNum(CPF):
    mult = 1; soma = 0; i = 10
    for digito in CPF[:9]:
        mult = int(digito) * i
        soma += mult
        i -= 1
    resultado = 11 - (soma % 11)
    if resultado > 9: resultado = 0
    return resultado

def ultNum(CPF):
    mult = 1; soma = 0; i = 11
    for digito in CPF[:9]:
        mult = int(digito) * i
        soma += mult
        i -= 1
    soma += priNum(CPF) * 2
    resultado = 11 - (soma % 11)
    if resultado > 9: resultado = 0
    return resultado

def validaNum(CPF):
    for digito in CPF:
        try:
            int(digito)
        except:
            return False
    return True

def numIguais(CPF):
    digitoUm = CPF[0]
    for digito in CPF:
        if digito != digitoUm:
            return False
    return True

def valida(CPF):
    if validaNum(CPF) and not(numIguais(CPF)):
        cpf = CPF[:-2]
        cpf += str(priNum(CPF))
        cpf += str(ultNum(CPF))
        if cpf == CPF and len(CPF) == 11:
            return True
    messagebox.showerror("Atenção", "CPF inválido")
    return False