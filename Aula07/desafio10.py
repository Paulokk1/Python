wallet = float(input('Quanto vc tem na carteira? R$'))
print('Considerando o dolar a US$1 = R$ 5,29')
dolar = wallet / 5.29
print('Você terá: US${:.2f}'.format(dolar))