import random
no1 = input('Digite um nome para ser sorteado: ')
no2 = input('Digite um nome para ser sorteado: ')
no3 = input('Digite um nome para ser sorteado: ')
lis = [no1, no2, no3]
ram = random.choice(lis)

print('{} foi o nome sorteado'.format(ram))