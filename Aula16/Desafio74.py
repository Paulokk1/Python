from random import randint
nums = ()

for c in range(0, 5):
    num = randint(1, 100)
    nums += (num,)
print(f'Números sorteados: {nums}')
print(f'O maior valor: {max(nums)}')
print(f'O menor valor: {min(nums)}')