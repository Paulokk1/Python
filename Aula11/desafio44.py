produto = float(input('Qual o valor do produto? '))
print('Escolha o método de pagamento:')
print('[ 1 ] Dinheiro/cheque (10% de desconto)')
print('[ 2 ] Á vista no cartão (5% de desconto)')
print('[ 3 ] Cartão 2x (preço normal)')
print('[ 4 ] Cartão 3x ou mais (20% de juros)')
pagamento = int(input('Digite o método de pagamento: '))
if pagamento == 1:
    print('Escolhendo o método dinheiro/cheque o produto saíra com 10% de desconto')
    print('Valor final R${}'.format(produto - (produto * 10 / 100)))
elif pagamento == 2:
    print('Escolhendo o método á vista no cartão o produto saíra com 5% de desconto')
    print('Valor final R${}'.format(produto - (produto * 5 / 100)))
elif pagamento == 3:
    print('Escolhendo o método 2x no cartão o produto saíra com o valor normal')
    print('Valor final R${}'.format(produto))
elif pagamento == 4:
    print('Escolhendo o método 2x no cartão o produto saíra com o valor normal')
    print('Valor final R${}'.format(produto + (produto * 20 / 100)))
