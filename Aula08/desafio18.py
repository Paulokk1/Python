import math

an = float(input('Digite um ângulo: '))
seno = math.sin(math.radians(an))
cosseno = math.cos(math.radians(an))
tangente = math.tan(math.radians(an))
print('O Seno de {} é: {:.2f}'.format(an, seno))
print('O Cosseno de {} é: {:.2f}'.format(an, cosseno))
print('O Tangente de {} é: {:.2f}'.format(an, tangente))