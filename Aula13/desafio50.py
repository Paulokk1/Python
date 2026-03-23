soma = 0
print('Aparecerá 6 valores para você digitar o programa deve ler os númeors pares e soma-los, os impares ignorar')
for n in range(1, 7):
    number = int(input('Digite um valor: '))
    par = number % 2
    if par == 0:
        soma = number + soma
print('Soma final {}'.format(soma))