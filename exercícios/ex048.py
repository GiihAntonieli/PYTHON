soma = 0
c = 0
for count in range(1, 501, 2):
    if count % 3 == 0:
        c = c + 1
        soma = soma + count
print('A soma de todos os {} valores solicitados é de {}' .format(c, soma))









