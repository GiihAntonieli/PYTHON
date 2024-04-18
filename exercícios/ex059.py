from time import sleep
n1 = int(input('Digite um valor: '))
n2 = int(input('Digite um segundo valor: '))
p = 0
while p != 5:
    print(''' 
    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Maior
    [ 4 ] Novos Números
    [ 5 ] Sair do Programa''')
    p = int(input('>>>>> Qual operação você deseja realizar: '))

    if p == 1:
        c = n1 + n2
        print('A soma entre {} + {} é {}'.format(n1, n2, c))
    elif p == 2:
        c = n1 * n2
        print('A multiplicação entre {} x {} é {}'.format(n1, n2, c))
    elif p == 3:
        if n1 > n2:
            print('{} é o maior'.format(n1))
        elif n1 < n2:
            print('{} é o maior' .format(n2))
        else:
            print('{} e {} são iguais.'.format(n1, n2))
    elif p == 4:
        n1 = int(input('Digite um valor: '))
        n2 = int(input('Digite um segundo valor: '))
    elif p == 5:
        print('Finalizando...')
    else:
        print('Opção Inválida. Tente novamente!')
    print('=-=' * 10)
    sleep(2)
print('FIM do Programa! Volte sempre!')