import time
valor = int(input('Digite um valor: '))
contagem = 1
print('Os números pares de 1 a {} são:'.format(valor))
for m in range(0, valor):
    par = contagem % 2
    if par == 0:
        print(contagem)
        time.sleep(0.3)
    contagem = contagem + 1