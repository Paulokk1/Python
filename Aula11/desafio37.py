numero = int(input('Qual o valor do seu número: '))
print('[ 1 ] converter para Binário')
print('[ 2 ] converter para Octal')
print('[ 3 ] converter para Hexadecimal')
res = int(input('Qual o valor escolhido: '))
if res == 1:
    print('O valor em binário é {}'.format(bin(numero)[2:]))
elif res == 2:
    print('O valor em octal é {}'.format(oct(numero)[2:]))
elif res == 3:
    print('O valor hexadecimal é {}'.format(hex(numero)[2:])) 
else:
    print('Opção invalida')