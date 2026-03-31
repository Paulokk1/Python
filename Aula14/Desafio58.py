import random
import time
aleaT = random.randint(1, 10)
n1 = 0
cont = 0
for n in range(1, 4):
    print('{}...'.format(n))
    time.sleep(0.5)
print('Tente acertar o número que estou pensando!')
while n1 != aleaT:
    n1 = int(input('Digite um número: '))
    cont += 1
    print('Errou, tente de novo!')
print('Você acertou! Total de tentativas: {}'.format(cont))