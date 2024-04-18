from random import randint
from time import sleep
lista = list()
jogos = list()
print("-"*40)
print("           JOGA NA MEGA SENA           ")
print("-"*40)
quant = int(input('Quantos jogos vc quer que eu sorteie: '))
tot = 1
while tot <= quant:
    cont = 1
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print('-='*3, f"SORTEANDO {quant} JOGOS", '-=' * 3)
for i , l in enumerate(jogos):
    print(f'Jogo {i}: {l}')
    sleep(0.7)
print('-='*5, '< BOA SORTE! >', '-='*5)
#print(f'Os números sorteados foram {jogos}')

