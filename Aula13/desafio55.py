peso = []
for n in range(5):
    resp = int(input('Me fale o pseo dá {} pessoa: '.format(n + 1)))
    peso.append(resp)
maior = max(peso)
menor = min(peso)
print('Maior peso é {}kg\nMenor peso é {}kg'.format(maior, menor))
