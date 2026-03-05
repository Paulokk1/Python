import random
repetir = 1
while repetir == 1:
    jokenpo = random.randint(1, 3)
    print('vamos jogar pedra papel tesoura? ')
    print('[ 1 ] pedra ' \
    '[ 2 ] tesoura ' \
    '[ 3 ] papel ')
    res = int(input('Qual vc escolhe? '))
    if res == 1 and jokenpo == 1:
        print('PEDRA!')
        print('Empatou! Digite "1" para repetir ')
    elif res == 1 and jokenpo == 2:
        print('TESOURA!')
        print('Ganhou! Digite "1" para repetir ')
    elif res == 1 and jokenpo == 3:
        print('PAPEL!')
        print('Perdeu! Digite "1" para repetir ')


    elif res == 2 and jokenpo == 1:
        print('PEDRA!')
        print('Perdeu! Digite "1" para repetir ')
    elif res == 2 and jokenpo == 2:
        print('TESOURA!')
        print('Empate! Digite "1" para repetir ')
    elif res == 2 and jokenpo == 3:
        print('PAPEL!')
        print('Ganhou! Digite "1" para repetir ')

    elif res == 3 and jokenpo == 1:
        print('PEDRA!')
        print('Ganhou! Digite "1" para repetir ')
    elif res == 3 and jokenpo == 2:
        print('TESOURA!')
        print('Perdeu! Digite "1" para repetir ')
    elif res == 3 and jokenpo == 3:
        print('PAPEL!')
        print('Empate! Digite "1" para repetir ')

    repetir = int(input(''))
print('Foi um bom jogo!')