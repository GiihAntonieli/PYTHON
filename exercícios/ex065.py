r = 'S'
c = soma = maior = menor = 0
while r == 'S':
    n = int(input('Digite um número: '))
    c += 1
    soma += n
    if c == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    r = str(input('Quer continuar: [S,N] ')).strip().upper()
media = soma / c
print('Você digitou {} nímeros e a média foi {:.2f}' .format(c, media))
print('{} é o maior valor e {} é o menor valor' .format(maior, menor))