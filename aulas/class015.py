n = s = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n
print('A soma vale {}' .format(s))# PYTHON 3
#print(f'A soma vale {s}') PYTHON 3.06
#print('A soma vale %d' %s) PYTHON 2

