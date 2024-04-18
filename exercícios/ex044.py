print('========== LOJAS ANTONIELI ==========')
compra = float(input('Preço das compras: R$'))
print('''
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista no cartão
[ 3 ] 2x no cartão 
[ 4 ] 3x ou mais no cartão''')
opçao = int(input('Qual é a opção? '))

if opçao == 1:
    saldo = compra - (compra * 10 / 100)
    print('Sua compra é de {:2.f} e com os 10% de desconto fica {:.2f}.' .format(compra, saldo))

elif opçao == 2:
    saldo = compra - (compra * 5 / 100)
    print('Sua compra é de {:.2f} e com os 5% de desconto fica {:.2f}.'.format(compra, saldo))

elif opçao == 3:
    parcela = compra / 2
    print('Sua compra será parcelada em 2x de R${:.2f}' .format(parcela))

elif opçao == 4:
    saldo = compra + (compra * 20 / 100)
    parcelas = int(input('Quantas parcela? '))
    parc = saldo / parcelas
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS' .format(parcelas, parc))
    print('Sua compra de R${:.2f}vai custar R${:.2f} no final.' .format(compra, saldo))

else:
    total = 0
    print('OPÇÃO INVÁLIDA de pagamento. Tente novamente!')






