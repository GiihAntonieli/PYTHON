print('Gerador de PA')
print('-=' * 15)
t1 = int(input('Primeiro termo: '))
r = int(input('Razão da PA: '))
termo = t1
c = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while c <= total:
        print('{} -> ' .format(termo), end='')
        termo = termo + r
        c += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais: '))
print('Progressão finalizada com {} mostrados.' .format(c))