sexo = 'k'
while sexo != 'M' and sexo != 'F':
    sexo = str(input('Qual o seu sexo[M/F]: ')).upper().strip()
    sexo = sexo[0]
print('Sexo armazenado!')