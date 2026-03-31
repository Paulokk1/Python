cont = 0
soma = 0
pa = int(input('Primeiro termo da PA: '))
razao = int(input('Qual a razão da PA: '))
while cont != 10:
    cont += 1
    pa = pa + razao
    print('{}° termo: {}'.format(cont, pa))
