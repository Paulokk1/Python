soma = 0
contador = 0
quantidade = 500

for n in range(0, quantidade):
    impar = contador % 2
    if impar == 1:
        multipl0 = contador % 3
        if multipl0 == 0:
            soma = contador + soma
    contador += 1


print('A soma de todos os valores impares multiplos de 3 é {}'.format(soma))