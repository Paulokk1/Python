termo = int(input('primeiro termo da PA: '))
razao = int(input('razão da PA: '))
cont = 1
for n in range(1, 11):
    print('{}° termo: {}'.format(cont, termo))
    termo = termo + razao
    cont += 1