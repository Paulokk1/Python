number = int(input('Escolha um número para a tabuada: '))
for n in range(1, 11):
    print('{} x {} = {}'.format(number, n, number * n))