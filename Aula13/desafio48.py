qauntidade = 500
contador = 0
soma = 0
for n in (0, qauntidade):
    impar = contador % 2
    if  impar == 1:
        multiplo = impar % 3
    elif multiplo == 0:
        soma = contador + soma
    contador += 1
