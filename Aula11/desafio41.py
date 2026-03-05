import datetime
nascimento = int(input('Qual seu ano de nascimento? '))
idade = datetime.date.today().year - nascimento
if idade <= 9:
    print('Classificação: Mirim')
elif idade <= 14:
    print('Classificação: Infantil')
elif idade <= 19:
    print('Classificação: Junior')
elif idade == 20:
    print('Classificação: Sênior')
elif idade > 20:
    print('Classificação: Master')





