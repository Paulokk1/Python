res = 0
while res != 5:
    n1 = int(input('Digite o primeiro valor: '))
    n2 = int(input('Digite o segundo valor: '))
    print(' [1] SOMA \n [2] MULTIPLICAR \n [3] MAIOR \n [4] NOVOS NÚMEROS \n [5] SAIR DO PROGRAMA')
    res = int(input('Sua escolha: '))
    if res == 1:
        print('Resultado dá soma: {}'.format(n1 + n2))
    if res == 2: 
        print('Resultado da multiplicação: {}'.format(n1 * n2))
    if res == 3:
        if n1 > n2:
            print('Maior número: {}'.format(n1))
        else:
            print('Maior número: {}'.format(n2))
    
    elif res != 4:
        res = str(input('Quer fechar o programa[S/N]: ')).upper()
        if res == 'S':
            res = 5
        else:
            res = 3
    
print('Saindo do programa!')