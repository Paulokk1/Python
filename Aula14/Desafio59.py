n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
while True:
    
    print('[1] SOMA \n [2] Multiplicação \n [3] MAIOR \n [4] NOVOS NÚMEROS \n [5] SAIR DO PROGRAMA')


    escolha = int(input('Qual opção você escolhe? '))


    if escolha == 1:
        soma = n1 + n2
        print('A soma de {} + {} é: {}'.format(n1, n2, soma))
    
    elif escolha == 2:
        multi = n1 * n2
        print('A multiplicação de {} + {} é: {}'.format(n1, n2, multi))

    elif escolha == 3:
        if n1 > n2:
            print('Maior valor é: {}'.format(n1))
        else:
            print('Menor valor é: {}'.format(n2))
    elif escolha == 4:
        n1 = int(input('Digite o primeiro valor: '))
        n2 = int(input('Digite o segundo valor: '))
    elif escolha == 5:
        break
    else:
        print('Opção invalida')


    fechar = str(input('Quer fechar o programa [S/N]? ')).upper().strip()[0]
    if fechar == 'S':
        break