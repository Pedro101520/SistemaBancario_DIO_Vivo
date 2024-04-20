def priNum(CPF):
    mult = 1; soma = 0; i = 10
    for digito in CPF[:9]:
        mult = int(digito) * i
        soma += mult
        i -= 1
    return 11 - (soma % 11)

def ultNum(CPF):
    mult = 1; soma = 0; i = 11
    for digito in CPF[:9]:
        mult = int(digito) * i
        soma += mult
        i -= 1
    soma += priNum(CPF) * 2
    return 11 - (soma % 11)

def valida(CPF):
    print(priNum(CPF))
    print(ultNum(CPF))