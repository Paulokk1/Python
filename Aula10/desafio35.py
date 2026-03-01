n1 = float(input('Digite o primeiro segmento de reta: '))
n2 = float(input('Digite o segundo segmento de reta: '))
n3 = float(input('Digite o terceiro segmento de reta: '))
if n1 + n2 > n3 and n1 + n3 > n2 and n2 + n3 > n1:
    print('Pode se fazer um triângulo!')
else:
    print('Não se pode fazer um triângulo!')