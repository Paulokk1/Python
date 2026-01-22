nome = input('Qual o seu nome? ')
print('Prazer em conhecer {:~^20}'.format(nome))

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
print('Resultados: \n soma: {} \n Subtração: {} \n multiplicação: {} \n'.format(n1 + n2, n1 - n2, n1 * n2), end= '>>')