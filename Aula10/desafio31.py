n1 = int(input('Qual a distância da viagem? '))
if n1 > 200:
    n2 = n1 * 0.45
    print('Sua viagem custará: {} pois acima de 200km, o valor por km é 0,45'.format(n2))
else:
    n3 = n1 * 0.50
    print('Sua viagem custará: {} pois abaixo de 200km, o valor por km é 0,50'.format(n3))