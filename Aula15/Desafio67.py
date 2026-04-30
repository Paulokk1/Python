c = 1


print('=' * 60)
print('Números negativos param o program!')
print('=' * 60)
while True:
    n1 = int(input('A tabuada de qual valor? '))
    if n1 < 0:
        break
    while c < 11:
        multiplicao = n1 * c
        print('{} x {} = {}'.format(n1, c, multiplicao))
        
        c += 1
    c = 1
    