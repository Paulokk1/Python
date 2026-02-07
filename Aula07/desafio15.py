Dias = int(input('Por quantos dias o carro foi alugado? '))
Km = int(input('Quantos Kms rodados? '))
Pdias = Dias * 60
Pkm = Km * 0.15
print('O custo total foi {}'.format(Pdias + Pkm))