import random
from time import sleep
lista = [0,1,2]
computador = random.choice(lista)
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogada = int(input('Qual é a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!!!')
print('-=' *11)
print('Computador jogou {}' .format(jogada))
print('Jogador jogou {}' .format(lista[computador]))
print('-=' * 11)

if jogada == 0:
    if computador == 0:
        print('EMPATE!')
    elif computador == 1:
        print('Computador GANHOU!')
    elif computador == 2:
        print('Você GANHOU!!')
elif jogada == 1:
    if computador == 0:
        print('Você GANHOU!!')
    elif computador == 1:
        print('EMPATE!')
    elif computador == 2:
        print('Computador GANHOU!')
elif jogada == 2:
    if computador == 0:
        print('Computador GANHOU!')
    elif computador == 1:
        print('Você GANHOU!!')
    elif computador == 2:
        print('EMPATE!')
else:
    total = 0
    print('Jogada INVÁLIDA. Tente novamente!')



from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print(''' Suas opções: 
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual é a sua jogada: '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!!!')
print('-=' *11)
print('Computador jogou {}' .format(itens[computador]))
print('Jogador jogou {}' .format(itens[jogador]))
print('-=' * 11)

if jogador == 0:
    if computador == 0:
        print('EMPATE!')
    elif computador == 1:
        print('Computador GANHOU!')
    elif computador == 2:
        print('Você GANHOU!!')
elif jogador == 1:
    if computador == 0:
        print('Você GANHOU!!')
    elif computador == 1:
        print('EMPATE!')
    elif computador == 2:
        print('Computador GANHOU!')
elif jogador == 2:
    if computador == 0:
        print('Computador GANHOU!')
    elif computador == 1:
        print('Você GANHOU!!')
    elif computador == 2:
        print('EMPATE!')
else:
    total = 0
    print('Jogada INVÁLIDA. Tente novamente!')






