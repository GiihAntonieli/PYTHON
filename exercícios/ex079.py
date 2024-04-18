valores = list()

while True:
    n = int(input('Digite um valor: '))
    if n not in valores:
        valores.append(n)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')

    # resposta e
    resp = str(input('Quer continuar: [S/N] ')).upper()

    if resp == 'N':
        break

    # Minha resposta para verificar se podia acrescentar mais um valor ou não
    '''if resp == 'S':
        valores.append(int(input('Digite um valor: ')))
    else:
        print('Resposta ERRADA! Tente S para SIM ou N para NÃO!!!!')
        resp = str(input('Quer continuar: [S/N] ')).upper()
        valores.append(int(input('Digite um valor: ')))'''

    # Tentativa de verificar números duplicados
    '''if valores in valores: #Barreira para números iguais#
            print('Valor duplicado! Não vou adicionar...')'''

print('=-'*40)
print('FIM da Lista')
print('=-'*40)
valores.sort()
print(f'Você digitou os valores {valores}')
print('-'*40)
