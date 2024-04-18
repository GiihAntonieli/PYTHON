print('Gerador de PA')
print('-=' * 10)
t1 = int(input('Primeiro termo: '))
r = int(input('Razão da PA: '))
termo = t1
c = 1

while c <= 10:
    print('{} -> ' .format(termo), end='')
    termo = termo + r
    c += 1
print('ACABOU!')
