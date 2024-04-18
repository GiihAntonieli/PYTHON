import random
n1 = str(input('Digite seu nome: '))
n2 = str(input('Digite seu nome: '))
n3 = str(input('Digite seu nome: '))
n4 = str(input('Digite seu nome: '))
lista = [n1, n2, n3, n4]
random.shuffle(lista)
print('A ordem dos alunos é: ')
print(lista)
