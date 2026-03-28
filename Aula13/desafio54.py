import datetime
nascimento = []
maior18 = 0
menor18 = 0
anoatual = datetime.datetime.now().year
for n in range(7):
    resp = int(input('Data de nascimento {}º pessoa: '.format(n + 1)))
    if resp >= 2026 or resp <= 1000:
        print('Resposta invalida!')
        exit()
    nascimento.append(resp)
for i in range(7):
    if anoatual - nascimento[i] >= 18:
        maior18 += 1
    elif anoatual - nascimento[i] < 18:
        menor18 += 1

print('Pessoas com mais de 18 anos: {} pessoas. ' \
'Pessoas com menos de 18 anos: {} pessoas'.format(maior18, menor18))
