
print("=" * 60)
print(" " * 25, "BANCO", " " * 45)
print("=" * 60)
valor = int(input('Qual o valor a ser sacado? '))

resto = valor

#Variaveis
total50 = 0
ce50 = 0

total20 = 0
ce20 = 0

total10 = 0
ce10 = 0

total1 = 0
ce1 = 0


while resto >= 50:
    resto -= 50
    total50 += 50
    ce50 += 1
while resto >= 20:
    resto -= 20
    total20 += 20
    ce20 += 1
while resto >= 10:
    resto -= 10
    total10 += 10
    ce10 += 1
while resto >= 1:
    resto -= 1
    total1 += 1
    ce1 += 1


print(f"São {ce50} cédulas de R$50, totalizando: R${total50}")
print(f"São {ce20} cédulas de R$20, totalizando: R${total20}")
print(f"São {ce10} cédulas de R$10, totalizando: R${total10}")
print(f"São {ce1} cédulas de R$01, totalizando: R${total1}")
print("=" * 60)