print('Calculo de IMC, saiba a sua classificação de peso!')
peso = float(input('Qual o seu peso? '))
altura = float(input('Qual sua altura? '))
imc = peso / (altura ** 2)
if imc < 18.5:
    print('Abaixo do peso! Classificação IMC: {:.2f}'.format(imc))
elif imc <= 24.9:
    print('Peso normal! Classificação IMC: {:.2f}'.format(imc))
elif imc < 29.9:
    print('sobrepeso! Classificação IMC: {:.2f}'.format(imc))
elif imc <= 39.9:
    print('Obesidade! Classificação IMC: {:.2f}'.format(imc))
elif imc > 40:
    print('Obesidade grave! Classificação IMC: {:.2f}'.format(imc))
else:
    print('Valores incorretos! Classificação IMC: {:.2f}'.format(imc))