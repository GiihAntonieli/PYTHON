'''num = [[], []]
valor = 0
for n in range(1, 8):
    valor = int(input(f'Digite o {n}o número: '))
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)
'''

numero = list()
pares = list()
impares = list()

numero.append(pares[:])
numero.append(impares[:])
for n in range(1, 8):
    num = int(input(f'Digite o {n}o número: '))
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num
print('-=' * 40)
#numero.sort()
print(num)
pares.sort()
print(pares)
impares.sort()
print(impares)

