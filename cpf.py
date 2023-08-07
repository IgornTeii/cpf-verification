def valida1(n1):
    soma = digito = resto = 0
    cont = 10
    for i in n1:
        soma += i * cont
        cont -= 1
resto = soma % 11
if resto < 2:
    digito = 0
else 
    digito = 11 - resto
return digito


#programa principal
cpfnum = []
print("Digite seu CPF (somente numeros)")
cpf = input()
for i in range(0,9,1):
    cpfnum.append(int(cpf[i:i+1]))
#print(cpfnum)

