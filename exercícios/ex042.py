r1 = float(input('Primeiro Segmento: '))
r2 = float(input('Segundo Segmento: '))
r3 = float(input('Terceiro Segmento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    if r1 == r2 == r3:
        print('É POSSÍVEL haver um triângulo EQUILÁTERO!')
    elif r1 != r2 != r3 != r1:
        print('É POSSÍVEL haver um triângulo ESCALENO!')
    else:
        print('É POSSÍVEL haver um triângulo ISÓSCELES!')
else:
    print('NÃO É POSSÍVEL existir um triângulo!')








