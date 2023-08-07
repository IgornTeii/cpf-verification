def valida1(n1, x):
    soma = digito = resto = 0
    cont = x
    for i in n1:
        soma += i * cont
        cont -= 1
    resto = soma % 11
    if resto < 2:
        digito = 0
    else :
        digito = 11 - resto
    return digito

#programa principal

cpfnum = []
digiuno = digidou = 0 
print("Digite seu CPF (somente numeros)")
cpf = input()
for i in range(0,9,1):
    cpfnum.append(int(cpf[i:i+1]))
digiuno =valida1(cpfnum, 10)
cpfnum.append(digiuno)
digidou = valida1(cpfnum, 11)
cpfnum.append(digidou)
print(cpfnum)



