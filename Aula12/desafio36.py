n1 = int(input('Qual o valor do imovel: R$'))
n2 = int(input('Qual o seu sálario: R$'))
anos = int(input('Quantos anos de financiamento: '))
calc = n1 / (anos * 12) 
calc2 = (30 * n2) / 100
print('Para pagar um imovel de R${} em {} anos a prestação seria de R${:.2f}'.format(n1, anos, calc))
if calc > calc2:
    print('Acesso negado, o valor ultrapassa 30% do seu sálario')
else:
    print('Acesso permitido!!!')