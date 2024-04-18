viagem = float(input('Digite a distância da sua viagem em km: '))
if viagem <= 200:
    passagem = viagem * 0.50
    print('Sua passagem vai custar R${:.2f}'.format(passagem))
else:
    passagem = viagem * 0.45
    print("Sua passagem irá custar R${:.2f}" .format(passagem))
