primo = True
num = int(input('Digite um valor: '))
for n in range(2, num):
    if num % n == 0:
        primo = False
        break
if primo == True:
    print('Número primo!')
if primo == False:
    print('Não é primo!')