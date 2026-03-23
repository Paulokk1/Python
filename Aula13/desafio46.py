import time
print('Os fogos de artifício vão começar')
contagem = 1
for m in range(0, 10):
    print(contagem)
    time.sleep(1)
    contagem = contagem + 1
print('=' * 35)
print('Explosão!!')
print('=' * 35)