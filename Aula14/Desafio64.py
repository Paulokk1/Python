soma = 0
cont = 1
while True:
    digit = int(input('Digite um número [999 para parar]'))
    if digit == 999:
        cont = cont - 1
        break
    soma += digit
    cont += 1

    

print('Você digitou {} números e a soma entre eles foi {}'.format(cont, soma))