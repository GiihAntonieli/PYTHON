print('ESCOLHA UMA BASE DE CONVERSÃO: ')
num = int(input('Digite um número inteiro: '))
print('[ 1 ] converter para BINÁRIO')
print('[ 2 ] converter para OCTAL')
print('[ 3 ] converter para HEXADECIMAL')
escolha = int(input('Sua opção: '))

if escolha == 1:
    print('{} é o número BINÁRIO de {}.' .format(bin(num)[2:], num))
elif escolha == 2:
    print('{} é o número em OCTAL de {}' .format(oct(num)[2:], num))
elif escolha == 3:
    print('{} é o número em HEXADECIMAL de {}' .format(hex(num)[2:], num))
else:
    print('Opção INVÁLIDA! Tente novamente.')
















