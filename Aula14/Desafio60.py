cont = 1
final = perg = int(input('Qual o valor que será fatorial: '))
while cont != final:
    if cont == 1:
        soma = final * (final - 1)
        perg = perg - 1

    perg = perg - 1
    if perg == 0:
        perg = 1

    soma = soma * perg

    cont += 1
print('Resultado do seu fatorial {}! é {}'.format(final, soma))