import random
no1 = input('Digite um nome: ')
no2 = input('Digite um nome: ')
no3 = input('Digite um nome: ')
no4 = input('Digite um nome: ')

lis = [no1, no2, no3, no4]
random.shuffle(lis)
print('A ordem será:')
print(lis)