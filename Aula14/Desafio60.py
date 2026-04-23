cont = 1
c = final = perg = int(input('Qual o valor que será fatorial: '))

while cont != final:
    if cont == 1:
        soma = final * (final - 1)
        perg = perg - 1

    perg = perg - 1
    if perg == 0:
        perg = 1

    soma = soma * perg

    cont += 1
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ' , end='')
    c -= 1
print(soma)

print('\nResultado do seu fatorial {}! é {}'.format(final, soma))
print('=' * 50)