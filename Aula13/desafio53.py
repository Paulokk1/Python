frase = str(input('Me diga uma palavra: ')).lower().split()
junto = ''.join(frase)
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
print('Você digitou: {}. Ao contrário: {}'.format(junto, inverso))
if junto == inverso:
    print('É um palíndromo!')
else:
    print('não é um palídromo!')
    
