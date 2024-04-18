from random import randint
computador = randint(0, 10)
print('Sou seu computador...')
print('''Acabei de pensar em um número entre 0  e 10.
Será que você consegue adivinhar qual foi? ''')

c = 0

acertou = False
while not acertou:
    palpite = int(input('Qual é o seu palpite? '))
    c += 1
    if palpite == computador:
        acertou = True
    else:
        if palpite > computador:
            print('Menos... Tente mais uma vez!')
        elif palpite < computador:
            print('Mais... Tente mais uma vez.')
print('Acertou com {} tentativas. Parabéns!' .format(c))
