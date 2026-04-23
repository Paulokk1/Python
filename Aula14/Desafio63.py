n1 = 0
n2 = 1
cont = 1
print('-' * 60)
termos = int(input('Quantos termos da sequência de Fibonacci vc quer fer? ')) - 1
print('-' * 60)
print('{} --> \n{} -->'.format(n1, n2), end='')
while cont != termos:
    soma = n1 + n2
    n1 = n2
    n2 = soma
    

    cont +=1
    print(soma , ' --> ' if cont != termos else '!', end='')