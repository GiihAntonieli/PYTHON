valores = list()
mai = 0
men = 0
for cont in range(0, 5):
    valores.append(int(input(f'Digite um valor para a Posição {cont}: ')))
    if cont == 0:
        mai = men = valores[cont]
    else:
        if valores[cont] > mai:
            mai = valores[cont]
        if valores[cont] < men:
            men = valores[cont]

print('=-'*30)
print('FIM da Lista!')
print('=-'*30)
print(f'Você digitou os valores {valores}')
print(f'{max(valores)} é o maior valor digitado nas posições.', end='')
for i, v in enumerate(valores):
    if v == mai:
        print(f'{i}...', end='')
print(f'\n {min(valores)} é o menor valor digitado nas posições.', end='')
for i, v in enumerate(valores):
    if v == men:
        print(f'{i}...')
print('-'*30)
