import random
import time
c1 = 0

escolha = str(input('Você quer par ou impar[P/I]? ')).upper().strip()[0]
if escolha == 'P':
    while True:
        n1 = int(input('Escolha um valor: '))
        n2 = random.randint(1, 50)
        soma = n1 + n2
        print('Eu escolho...')
        time.sleep(3)
        print('{}!'.format(n2))
        if soma % 2 == 0:
            print("=" * 60)
            print('GANHOU')
            print("DEU PAR")
            print("=" * 60)
            c1 += 1    
        else:
            print("=" * 60)
            print('PERDEU')
            print("DEU IMPAR")
            print("=" * 60)
            break
        

if escolha == 'I':
    while True:
        n1 = int(input('Escolha um valor: '))
        n2 = random.randint(1, 50)
        soma = n1 + n2
        print('Eu escolho...')
        time.sleep(3)
        print('{}!'.format(n2))
        if soma % 2 == 0:
            print("=" * 60)
            print('PERDEU')
            print("DEU PAR")
            print("=" * 60)
            break
        else:
            
            print("=" * 60)
            print('GANHOU!')
            print("DEU IMPAR")
            print("=" * 60) 
            c1 += 1
print('Total de Vitorias: {}'.format(c1))