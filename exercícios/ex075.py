n = (int(input("Digite o primeiro valor: ")),
     int(input("Digite o segundo valor: ")),
     int(input("Digite o terceiro valor: ")),
     int(input("Digite o quarto valor: ")))
print(f'Você digitou os valores {n}')
print(f'O número 9 apareceu {n.count(9)} vezes')
if 3 in n:
    print(f'O número 3 fez sua primeira aparição na posição {n.index(3)+1}')
else:
    print('O valor 3 não apareceu em nenhuma posição')
print(f'Esses são os números pares ', end='')
for num in n:
    if num % 2 == 0:
        print(num, end=' ')


