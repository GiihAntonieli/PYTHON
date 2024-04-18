pessoas = list()
dados = list()
pesado = leve = 0
while True:
    dados.append(str(input('Digite seu nome: ')))
    dados.append(float(input('Digite seu peso: ')))
    if len(pessoas) == 0:
        pesado = leve = dados[1]
    else:
        if dados[1] > pesado:
            pesado = dados[1]
        if dados[1] < leve:
            leve = dados[1]
    pessoas.append(dados[:])
    dados.clear()
    resp = str(input('Você quer continuar? [S/N] ')).upper()
    if resp == 'S':
        print('Adicionado!!')
    elif resp == 'N':
        break
    else:
        while resp not in 'SN':
            print('Resposta ERRADA! tente responder S para SIM ou N para NÃO.')
            resp = str(input('Você quer continuar? [S/N] ')).upper()
            if resp == 'SN':
                break

print('-=' * 30)
print(f'Os dados foram {pessoas}')
print(f'Ao todo, você cadastrou {len(pessoas)}.')
print(f'O maior peso foi de {pesado}Kg. Peso de ', end='')
for p in pessoas:
    if p[1] == pesado:
        print(f'[{p[0]}] ', end='')
print()
print(f'O menor peso foi de {leve}Kg. Peso de ', end='')
for p in pessoas:
    if p[1] == leve:
        print(f'[{p[0]}]', end='')

