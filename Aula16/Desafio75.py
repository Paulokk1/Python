n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite mais um número: '))
n4 = int(input('Digite o ultimo número: '))
par = 0
nums = ()
nums +=  (n1, n2, n3, n4)
print('=' * 60)
print(f'Os números digitados foram: {nums}')
print(f'O número 9 aparece {nums.count(9)} vezes')
if 3 in nums:
    print(f'O número 3 aparece na {nums.index(3) + 1}⁰ posição')
else:
    print(f'O número 3 aparece 0 vezes')
for num in range(4):
    if nums[num] % 2 == 0:
        par += 1
print(f'A quantidade de números pares: {par}')
print('=' * 60)