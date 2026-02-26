import random
print('Digite um número de 1 a 5 e tente adivinhar no que o computador pensou')
n1 = int(input('Qual número o computador pensou? '))
n2 = random.randint(1, 5)
if n1 == n2:
    print('Você acertou!!')
else:
    print('Você errou eu estava pensando em {}!'.format(n2))
