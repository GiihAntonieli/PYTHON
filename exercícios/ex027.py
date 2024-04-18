'''nome = str(input('Digite o seu nome completo: ')).strip()
primeiro = nome[0]
ultimo = nome [3]
print('Seu nome é {} ')
print('Primeiro: {}' .format(primeiro))
print('Último: {}' .format(ultimo))'''

n = str(input('Digite o seu nome completo: ')).strip()
nome = n.split()
primeiro = nome[0]
ultimo = nome[len(nome)-1]
print('Seu nome é {} ')
print('Primeiro: {}' .format(primeiro))
print('Último: {}' .format(ultimo))
