import random
import time
repetir = 1
while repetir == 1:
    jokenpo = random.randint(1, 3)
    print('vamos jogar pedra papel tesoura? ')
    print('[ 1 ] pedra ' \
    '[ 2 ] tesoura ' \
    '[ 3 ] papel ')
    res = int(input('Qual vc escolhe? '))
    print('JO')
    time.sleep(1.5)
    print('KEN')
    time.sleep(1.5)
    print('PO')
    if res == 1 and jokenpo == 1:
        print('=' * 30)
        print('Computador jogou: PEDRA!')
        print('Jogador jogou: PEDRA!')
        print('Empatou! Digite "1" para repetir ')
        print('=' * 30)
    elif res == 1 and jokenpo == 2:
        print('=' * 30)
        print('Computador jogou: TESOURA!')
        print('Jogador jogou: PEDRA!')
        print('Ganhou! Digite "1" para repetir ')
        print('=' * 30)
    elif res == 1 and jokenpo == 3:
        print('=' * 30)
        print('Computador jogou: PAPEL!')
        print('Jogador jogou: PEDRA!')
        print('Perdeu! Digite "1" para repetir ')
        print('=' * 30)


    elif res == 2 and jokenpo == 1:
        print('=' * 30)
        print('Computador jogou: PEDRA!')
        print('Jogador jogou: TESOURA!')
        print('Perdeu! Digite "1" para repetir ')
        print('=' * 30)
    elif res == 2 and jokenpo == 2:
        print('=' * 30)
        print('Computador jogou: TESOURA!')
        print('Jogador jogou: TESOURA!')
        print('Empate! Digite "1" para repetir ')
        print('=' * 30)
    elif res == 2 and jokenpo == 3:
        print('=' * 30)
        print('Computador jogou: PAPEL!')
        print('Jogador jogou: TESOURA!')
        print('Ganhou! Digite "1" para repetir ')
        print('=' * 30)

    elif res == 3 and jokenpo == 1:
        print('=' * 30)
        print('Computador jogou: PEDRA!')
        print('Jogador jogou: PAPEL!')
        print('Ganhou! Digite "1" para repetir ')
        print('=' * 30)
    elif res == 3 and jokenpo == 2:
        print('=' * 30)
        print('Computador jogou: TESOURA!')
        print('Jogador jogou: PAPEL!')
        print('Perdeu! Digite "1" para repetir ')
        print('=' * 30)
    elif res == 3 and jokenpo == 3:
        print('=' * 30)
        print('Computador jogou: PAPEL!')
        print('Jogador jogou: PAPEL!')
        print('Empate! Digite "1" para repetir ')
        print('=' * 30)

    repetir = int(input(''))
print('Foi um bom jogo!')