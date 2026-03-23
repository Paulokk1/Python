import datetime
atual = int(datetime.date.today().year)
nascimento = int(input('Em qual ano você nasceu? '))
idade = atual - nascimento
falta = 18 - idade
alistado = atual - (idade - 18)
print('Se você nasceu em {}, você tem {}'.format(nascimento, idade))
if nascimento > 2026:
    print('Ano de nascimento invalido')
elif idade < 18:
    print('Ainda vai se alistar, faltam {} anos para se alistar, seu alistamento será em {}'.format(falta, falta + atual))
elif 18 == idade:
    print('Está na hora de se alistar')
elif idade > 18:
    print('Já passou do tempo de se alistar, seu alistamento foi em {}'.format(alistado))
elif idade < 0:
    print('Ano de nascimento invalido')
else:
    print('Ano de nascimento invalido')