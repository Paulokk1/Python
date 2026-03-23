import datetime
nascimento = int(input('Qual seu ano de nascimento? '))
idade = datetime.date.today().year - nascimento
if idade <= 9:
    print('Sua idade é {}'.format(idade))
    print('Classificação: Mirim')
elif idade <= 14:
    print('Sua idade é {}'.format(idade))
    print('Classificação: Infantil')
elif idade <= 19:
    print('Sua idade é {}'.format(idade))
    print('Classificação: Junior')
elif idade == 20:
    print('Sua idade é {}'.format(idade))
    print('Classificação: Sênior')
elif idade > 20:
    print('Sua idade é {}'.format(idade))    
    print('Classificação: Master')





