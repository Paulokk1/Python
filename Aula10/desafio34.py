n1 = int(input('Qual o seu sálario? '))
print('Você receberá um aumento. Sendo superios a R$1250,00 aumento de 10%, inferios a R$1250,00 aumento de 15%')
calc10 = (n1 * 10 / 100) + n1
calc15 = (n1 * 15 / 100) + n1
if n1 >= 1250:
    print('O seu aumento será de 10%, seu novo sálario é {}'.format(calc10))
else:
    print('O seu aumento será de 15%, seu novo sálario é {}'.format(calc15))
