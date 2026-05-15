produtos = ()
c = 0
pergunta = ' '

while True:
    produtos += (str(input('Qual o nome do produto? ')),)
    produtos += (float(input('Qual o preço do produto?')),)
    while pergunta not in 'SN':
        pergunta = str(input('Você quer adicionar mais produtos? [S/N]: ')).strip().upper()[0]
    if pergunta == 'N':
        break
    pergunta = ' '

    
contidade = len(produtos)



print('=' * 60)
while c != contidade:
    print(f'{produtos[c]:.<20}', end='')
    c += 1
    print(f' R${produtos[c]}')
    c += 1
print('=' * 60)