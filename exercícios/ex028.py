import random
num = random.randint(0, 5)
tu = int(input('Aivinhe o número que o computador pensou: (DICA: está entre 0 e 5) '))
if tu == num:
    print("Acertou!!!!")
else:
    print('PERDEU, Tente mais tarde!')
print("Esse foi o número que o computador pensou ", num)

'''
from random import randint
computador = randint(0, 5) #Faz o computador 'PENSAR'
print('-=-' * 20)
print("Vou pensar em um número entre 0 e 5. Tente adivinhar...")
print('-=-' * 20)
jogador = int(input('Em que número eu pensei? ')) # jogador tenta adivinhar
if jogador == computador:
    '''



