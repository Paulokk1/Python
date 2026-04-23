pa = int(input('Qual o primeiro termo da pa? '))
razao = int(input('Qual a razão da pa? '))
rep = 11
c = 1
while c < rep:
    print('{} termo = {}'.format(c, pa))
    pa = pa + razao
    c += 1
pergunta = str(input('Você quer mais termos[S/N]? ')).upper().strip()[0]
if pergunta == 'S':
    termos = int(input('Quantos novos termos? '))
    rep = 11 + termos
    while c < rep:
        print('{} termo = {}'.format(c, pa))
        pa = pa + razao
        c += 1
        if c > rep:
            pergunta = str(input('Você quer mais termos[S/N]? ')).upper().strip()[0]
            if pergunta == 'S':
                termos = int(input('Quantos novos termos? '))
                rep = c + termos