soma = 0
cont = 1
todos = []
while True:
    n1 = int(input('Digite um número: '))
    parar = str(input('Quer continuar[S/N]? ')).upper()
    soma = n1 + soma
    media = soma / cont


    todos.append(n1)
    maior = max(todos)
    menor = min(todos)


    cont += 1


    if parar == 'N':
        break

print('A media dos valores foi: {} \nO maior número é {} e o menor número é {}'.format(media, maior, menor))