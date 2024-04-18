extenso = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco',
       'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze',
       'Doze', 'Treze','Quatorze', 'Quinze', 'Dezesseis',
       'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
num = int(input('Digite um número de 0 a 20: '))

while num < 0 or num > 20:
    print('Número inválido! Tente novamente '
          'com um número de 0 a 20.')
    num = int(input('Digite um número de 0 a 20: '))

if num == 0:
    print(extenso[0])
elif num == 1:
    print(extenso[1])
elif num == 2:
    print(extenso[2])
elif num == 3:
    print(extenso[3])
elif num == 4:
    print(extenso[4])
elif num == 5:
    print(extenso[5])
elif num == 6:
    print(extenso[6])
elif num == 7:
    print(extenso[7])
elif num == 8:
    print(extenso[8])
elif num == 9:
    print(extenso[9])
elif num == 10:
    print(extenso[10])
elif num == 11:
    print(extenso[11])
elif num == 12:
    print(extenso[12])
elif num == 13:
    print(extenso[13])
elif num == 14:
    print(extenso[14])
elif num == 15:
    print(extenso[15])
elif num == 16:
    print(extenso[16])
elif num == 17:
    print(extenso[17])
elif num == 18:
    print(extenso[18])
elif num == 19:
    print(extenso[19])
elif num == 20:
    print(extenso[20])

