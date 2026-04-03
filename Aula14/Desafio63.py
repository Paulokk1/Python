n1 = 0
n2 = 1
cont = 1
print('{} \n{}'.format(n1, n2))
while cont != 10:
    soma = n1 + n2
    n1 = n2
    n2 = soma
    print(soma)


    cont +=1