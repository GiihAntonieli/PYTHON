print('=' * 21)
print('10 TERMOS DE UMA PA')
print('=' * 21)
t = int(input('Primeiro termo: '))
r = int(input('Razão: '))
decimo = t + (11 - 1) * r
for c in range(t, decimo, r):
    print('{} '.format(c), end=', ')
print('ACABOU!')







