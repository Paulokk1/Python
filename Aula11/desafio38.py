n1 = int(input('Me fale um valor: '))
n2 = int(input('Agora um segundo valor: '))
if n1 > n2:
    print('O primeiro valor {}, é maior que o segundo {}'.format(n1, n2))
elif n2 > n1:
    print('O segundo valor {}, é maior que o segundo {}'.format(n2, n1))
else:
    print('Os 2 valores são iguais')