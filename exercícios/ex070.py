print('-' * 30)
print('{: ^30}' .format('LOJA SUPER BARATÃO'))
print('-' * 30)
c = 0
pmaior = 0
barato = 0
preçobarato = 0
compra = 0
while True:
    prod = str(input('Nome do Produto: ')).strip()
    preço = float(input('Preço: R$'))
    c += 1
    #total da compra
    compra = compra + preço

    #preço mais de 1000 reais
    if preço > 1000:
        pmaior += 1

    #produto mais barato
    if c == 1:#or prod < baarto
        barato = prod
        preçobarato = preço
    else:
        if prod < barato:
            barato = prod
            preçobarato = preço

    #resposta
    r = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    while r not in 'SN':
        r = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if r != 'S':
        break
print('{:-^40}' .format('FIM DO PROGRAMA'))
print(f'O total da compra foi R${compra:.2f}')
print(f'Temos {pmaior} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {barato} que custa R${preçobarato:.2f}')
