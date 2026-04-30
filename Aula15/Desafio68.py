import random
import time
c1 = 1

escolha = str(input('Você quer par ou impar[P/I]? ')).upper().strip()[0]
if escolha == 'P':
    while True:
        n1 = int(input('Ecolha um valor: '))
        n2 = random.randint(1, 50)
        soma = n1 + n2
        print('Eu escolho...')
        time.sleep(3)
        print('{}!'.format(n2))
        if soma % 2 == 0:
            print('Ganhou!')
            
        else:
            print('Perdeu')
            break
        c1 += 1

if escolha == 'I':
    while True:
        n1 = int(input('Ecolha um valor: '))
        n2 = random.randint(1, 50)
        soma = n1 + n2
        print('Eu escolho...')
        time.sleep(3)
        print('{}!'.format(n2))
        if soma % 2 == 0:
            print('Perdeu!')
            break
        else:
            print('Ganhou!')
            
            c1 += 1
print('Total de tentativas: {}'.format(c1))