c = 0
while True:
    t = int(input('Quer ver a tabuada de qual valor? '))
    print('-' * 30)
    if t < 0:
        break
    for c in range(1, 11):
        #m = t * c
        print(f'{t} x {c} = {t * c}')
        c += 1
    print('-' * 30)
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')