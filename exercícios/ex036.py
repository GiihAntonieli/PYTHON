valordacasa = float(input('Qual o valor da casa?:R$')) #100.000 reais
salario = float(input('Qual é o seu salário: R$')) #3.334 reais e 30% fica 1.000,02 reais de parcela
anos = int(input('Em quantos anos voçê irá querer pagar essa casa: ')) #8 anos e 3 meses

minimo = 30 * salario / 100
prestacao = valordacasa / (anos * 12)

if prestacao > minimo:
    print("Não será possível comprar está casa. Tente outra!")

else:
    print('Você tem condições de comprar esta casa!')

print('Para pagar uma casa de R${:.2f} em {} anos ' .format(valordacasa, anos), end='')
print(' a prestação será de R${:.2f}' .format(prestacao))












