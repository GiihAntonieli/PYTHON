ano = int(input('Digite um ano: '))
bissexto = ano % 4
if bissexto == 0:
    print('É um ano BISSEXTO !')
else:
    print('NÃo é um ano bissexto!')
