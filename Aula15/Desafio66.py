c = 0
soma = 0
while True:
    n1 = int(input('Digite um número[999 para parar]: '))
    n2 = n1
    if n1 == 999:
        break
    if c == 0:
        n2 = n2
        soma = n2
    else:
        soma = soma + n2
    
    c += 1

print('A soma dos {} foi {}'.format(c, soma))
    