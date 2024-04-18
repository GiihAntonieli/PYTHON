from random import randint
from time import sleep
lista = list()
jogos = list()
print("-"*40)
print('          JOGA NA MEGA SENA        ')
print("-"*40)
njogos = int(input('Quantos jogos vc quer que sejam gerados: '))
c = 1
while c <= njogos:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    c += 1
print('-=' * 3, f'SORTEANDO {njogos} JOGOS', '-=' * 3)
for i, l in enumerate(jogos):
    print(f'jogo {i+1}: {l}')
    sleep(1)
print('-='*5, '<BOA SORTE!>', '-='*5)
