sexo = ' '
Idade = 0
nome = ' '
conidade = 0
homens = 0
mulheresvin = 0
continuar = ' '
while True:    
    nome = str(input('NOME: '))
    Idade = int(input('IDADE: '))
    while sexo not in 'MF':
        sexo = str(input('SEXO: ')).upper().strip()[0]
    if Idade >= 18:
        conidade += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and Idade < 20:
        mulheresvin += 1 
    
    sexo = ' '
    while continuar not in 'SN':
        continuar = str(input('Você quer continuar?[S/N]: ')).upper().strip()[0]

    if continuar == 'N':
        break
    else:
        continuar = ' '


print(f'A quantidade de pessoas com mais de 18 é: {conidade}')
print(f'A quantidade de homens registrados é: {homens}')
print(f'A quantidade de mulheres com menos de 20 anos: {mulheresvin}')
