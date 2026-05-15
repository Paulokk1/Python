pergunta = 10
time = ' '
times = (
    "Palmeiras", "Flamengo", "Fluminense", "São Paulo", "Athletico-PR",
    "Bahia", "Bragantino", "Vasco da Gama", "Coritiba", "EC Vitória",
    "Cruzeiro", "Botafogo", "Atlético-MG", "Internacional", "Santos",
    "Corinthians", "Grêmio", "Mirassol", "Remo", "Chapecoense"
)



print('OS 5 primeiros colocados: 1 \nOs 4 ultimos colocados: 2 \nOS times em ordem alfabetica: 3 \nA posição do seu time: 4')


while pergunta > 4 or 1 > pergunta:
    pergunta = int(input('O que você quer ver? '))




if pergunta == 1:
    print(f'Os 5 primeiro colocados: ')
    print(times[0:5])
if pergunta == 2:
    print('Os 4 ultimos colocados')
    print(times[-4:])
if pergunta == 3:
    print('Os times em ordem alfabetica')
    print(sorted(times))
if pergunta == 4:
    while time not in times:
        time = str(input('Digite o nome do seu time para ver a posição dele: '))
    pos = times.index(time)
    print('Posição do seu time:')
    print(f'{times[pos]} {pos}⁰')