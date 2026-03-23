n1 = float(input('Digite o primeiro segmento de reta: '))
n2 = float(input('Digite o segundo segmento de reta: '))
n3 = float(input('Digite o terceiro segmento de reta: '))
if n1 + n2 > n3 and n1 + n3 > n2 and n2 + n3 > n1:
    print('Pode se fazer um \033[1;30;42mtriângulo!\033[m')
if n1 == n2 == n3:
    print('\033[1;36;41mTrângulo equilátero!\033[m')
elif n1 == n2 or n1 == n3 or n2 == n3:
    print('\033[1;36;41mTriâangulo isóceles!\033[m')
elif n1 != n2 and n1 != n3 and n2 != n3:
    print('\033[1;36;41mTriângulo Escaleno!\033[m')
else:
    print('Não se pode fazer um triângulo!')