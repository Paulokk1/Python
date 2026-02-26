vel = int(input('Qual a velocidade do seu carro neste momento? '))
multa = (vel * 7) - 560
if vel > 80:
    print('Você foi mmultado! O valor da multa é {}'.format(multa))
else:
    print('Você está na velocidade correta!')