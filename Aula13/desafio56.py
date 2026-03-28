nome = []
sexo = []
idade = []
idadesM = []
contadorf = 0
for i in range(4):
    print('-' * 10, i + 1, 'º' , 'pessoa' , '-' * 10)
    nome1 = str(input('Nome: '))
    idade1 = int(input('Idade: '))
    sexo1 = str(input('Sexo[M/F]: ')).lower()
    print('-' * 32)
    nome.append(nome1)
    sexo.append(sexo1)
    idade.append(idade1)


media = (idade[0] + idade[1] + idade[2] + idade[3]) / 4

for a in range(4):
    if sexo[a] == 'f':
        if idade[a] > 20:
            contadorf += 1
for n in range(4):
    if sexo[n] == 'm':
        idadesM.append(idade[n])        
        maior = max(idadesM)
posicao = idade.index(maior)

print('A média das idades é {}\nO homem com maior idade é: {}\nMulheres com mais de 20 anos: {}'.format(media, nome[posicao], contadorf))
