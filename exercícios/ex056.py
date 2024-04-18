totmaior = 0
totmenor = 0
imaior = 0
for p in range(1, 5):
    print('--------- {} PESSOA ----------' .format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: [F/M] ')).strip()

    imaior += idade
    media = imaior / 4

    if sexo == 'M' or 'm':
        if p == 1:
            totmaior = idade
        else:
            if idade > totmaior:
                totmaior = idade
                n = nome

    if sexo == 'F' or 'f':
        if idade < 20:
            totmenor += 1
print('')
print('A média de idade do grupo é de {} anos' .format(media))
print('{} é o nome do homem mais velho e ele possui {} anos' .format(n, totmaior))
print('{} mulheres tem menos de 20 anos' .format(totmenor))






