nota1 = int(input('Primeira nota: '))
nota2 = int(input('Segunda nota: '))
media = (nota1 + nota2) / 2
print('Tirando {} e {}, a média do aluno é {}'.format(nota1, nota2, media))
if media < 5:
    print('Você está reprovado')
elif media < 6.9:
    print('Você está de recuperação')
elif media >= 7:
    print('Você está aprovado')