valores = list()
pares = list()
impar = list()
valores.append(int(input('Digite um valor: ')))
while True:
    resp = str(input('Quer continuar: [S/N] ')).upper()
    if resp == 'S':
        valores.append(int(input('Digite um valor: ')))
    elif resp == 'N':
        break
    else:
        print('Resposta ERRADA! Tente S para SIM ou N para NÃO!!!!')
        resp = str(input('Quer continuar: [S/N] ')).upper()
        valores.append(int(input('Digite um valor: ')))
for c, v in enumerate(valores):
    if v % 2 == 0:
        pares.append(v)
    else:
        impar.append(v)
print('=-'*40)
print('FIM da Lista')
print('=-'*40)
print(f'A lista completa é {valores}')
print(f'A lista de pares é {pares}')
print(f'A lista de ímpares é {impar}')
print('-'*40)

