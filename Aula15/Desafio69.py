maior18 = 0
homensrg = 0
muie20 = 0
c = 1
pergunta = 'o'
while True:
    print(f'-------------{c}⁰pessoa----------------')
    nome = str(input(f'Nome dá {c}⁰ pessoa: '))
    idade = int(input(f'Qual a idade: '))
    sexo = str(input(f'Qual o sexo: ')).upper().strip()[0]

    if idade >= 18:
        maior18 += 1
    if sexo == 'M':
        homensrg += 1
    if idade > 18 and sexo == 'F':
        muie20 += 1
    c += 1
    if c > 2:
        while True:
            pergunta = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
            if pergunta == 'N':
                break
            if pergunta == 'S':
                break
    if pergunta == 'N':
        break
print(f'Pessoas com mais de 18: {maior18}')
print(f'Homens cadastrados: {homensrg}')
print(f'Mulheres com mais de 20 anos: {muie20}')