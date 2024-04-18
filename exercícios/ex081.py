valores = list()
valores.append(int(input('Digite um valor: ')))
while True:
    print('Valor adicionado com sucesso...')
    resp = str(input('Quer continuar: [S/N] ')).upper()
    if resp == 'S':
        valores.append(int(input('Digite um valor: ')))
    elif resp == 'N':
        break
    else:
        #print('Resposta ERRADA! Tente S para SIM ou N para NÃO!!!!')
        resp = str(input('Quer continuar: [S/N] ')).upper()
        valores.append(int(input('Digite um valor: ')))

print('=-'*40)
print('FIM da Lista')
print('=-'*40)
print(f'Você digitou esses valores {valores}')
print(f'{len(valores)} números foram digitados.')
valores.sort(reverse=True)
print(f'{valores} Essa é a lista em forma decrescente.')
if 5 in valores:
    r = 'Verdadeiro'
else:
    r = 'Falso'
print(f'O valor 5 está na lista? {r}')
print('-'*40)

