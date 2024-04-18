km = float(input('Qual a quantidade de Km percorridos? '))
dia = float(input('Qual a quantidade de dias? '))
aluguel = (km * 0.15)+(dia * 60)
print('Foram {} dias e {}Km percorridos e o preço do aluguel é R${}' .format(dia, km, aluguel))
