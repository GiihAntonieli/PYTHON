peso = float(input('Qual o seu peso? (Kg) '))
altura = float(input('Qual a sua altura? (m) '))

imc = peso / (altura**2)
print('O IMC dessa pessoa é de {:.1f}' .format(imc))

if imc < 18.5:
    print('ABAIXO do peso')
elif imc <= 25:
    print('Peso IDEAL')
elif imc <= 30:
    print('SOBREPESO')
elif imc <= 40:
    print('OBESIDADE')
else:
    print('Obesidade mórbida')










