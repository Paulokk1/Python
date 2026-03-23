valor = 50
contagem = 1
soma = 0
for m in range(0, valor - 1):
    impar = contagem % 2
    if impar == 1:
        multi3 = contagem % 3
    elif multi3 == 0:
        soma = soma + contagem
    contagem = contagem + 1
print('Soma de todos os números ímpares divisiveis por 3: {} {}'.format(soma, contagem))