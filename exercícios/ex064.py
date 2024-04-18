# n = c = soma = 0
n = 0
c = 0
soma = 0
while n != 999:
    n = int(input('Digite um número [999 para parar]: '))
    c += 1
    soma += n
    if n == 999:
        soma -= 999
        c -= 1
        print('Você digitou {} números e a soma entre eles foi {}.' .format(c, soma))
print('FIM')

'''
n = c = soma = 0
n = int(input('Digite um número [999 para parar]: '))
while n != 999:
    c += 1
    soma += n
    n = int(input('Digite um número [999 para parar]: '))
print('Você digitou {} números e a soma entre eles foi {}.' .format(c, soma))
print('FIM')
'''
