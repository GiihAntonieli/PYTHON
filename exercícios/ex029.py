km = float(input('Digite a velocidade do carro: '))
multa = (km - 80) * 7
if km > 80:
    print('você será multado! Sua multa será de: R${:.1f}' .format(multa))
else:
    print('Continue sua viagem!')
