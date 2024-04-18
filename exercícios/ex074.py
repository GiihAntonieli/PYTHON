from random import randint
n = (randint(1, 10), randint(1, 10), randint(1, 10),
    randint(1, 10), randint(1, 10))

print( 'Os valores sorteados foram: ', n)
#for c in range(0, len(n)):
#    print(n[c])
#    c += c
#    if n > c:
#        print('maior')
print(f'O maior valor é {max(n)}')
print(f'O menor valor é {min(n)}')
