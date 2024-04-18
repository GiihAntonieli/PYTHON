salario = float(input('Qual o valor do seu salario: '))
if salario <= 1.250:
    aumento = (salario * 10 / 100) + salario
    print('Seu salario depois do aumento de 10% ficara {}'  .format(aumento))
else:
    aumento = (salario * 15 / 100) + salario
    print('Seu salario depois do aumento de 15% ficara {}' .format(aumento))
