import time
ano = int(input('Qual ano você quer analisar? '))
print('PROCESSANDO...')
time.sleep(3)
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('Ano bissexto')
else:
    print('Não é bissexto')