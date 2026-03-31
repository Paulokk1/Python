cont = 0
rep = 0
cont2 = 0
pa = int(input('Primeiro termo da PA: '))
razao = int(input('Qual a razão da PA: '))
while cont != 10:
    cont += 1
    pa = pa + razao
    razaoamos = cont
    print('{}° termo: {}'.format(cont, pa))
while rep != 6:
    perg = str(input('Você quer mais termos[S/N]? ')).upper()
    if perg == 'S':
        razoes = int(input('Quantas razões? '))
        cont2 = cont
        razaoamos = razaoamos + razoes
    else:
        rep = 6
    while cont2 != cont + razoes:
        cont2 += 1
        pa = pa + razao
        razaoamos += 1
        print('{}° termo da razão: {}'.format(razaoamos, pa))