total = 0
menor = 0
c1000 = 0
c = 1
pergnta = ' '
print('-' * 70)
print(' ' * 25 ,  ' LOJA BARATÃO ' , ' ' * 30)
print('-' * 70)


while True:
    produto = str(input(f'Nome do {c}⁰ produto: '))
    preco = int(input(f'Preço do {c}⁰ produto: R$'))

    total = total + preco
    if c == 1:
        menor = preco
    if menor >= preco:
        menor = preco
        nomebarato = produto
    if preco > 1000:
        c1000 += 1

    while pergnta not in 'SN':
        pergnta = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if pergnta == 'N':
        break
    pergnta = ' '
    c += 1

print(f'Total gasto R${total}')
print(f'Produto mais barato: {nomebarato} R${menor}')
print(f'Produtos que custam mais de 1000: {c1000}')