c = 0
homem = 0
mulher = 0
i = 0
sexo = 'MF'
while True:
    print('-' * 30)
    print('CADASTRE UMA PESSOA')
    print('-' * 30)
    nome = str(input('Digite seu nome: '))
    # idade
    idade = int(input('Informe sua idade: '))
    if idade > 18:
        i += 1
    # sexo
    sexo = str(input('Informe seu sexo: [M/F]')).strip().upper()[0]
    if sexo == 'M':
        homem += 1
    elif sexo == 'F':
        if idade < 20:
            mulher += 1
    else:
        while sexo not in 'MF':
            sexo = str(input('Informe seu sexo: [M/F]')).strip().upper()[0]
    # resposta
    r = str(input('Deseja cadastrar mais uma pessoa? [S/N]')).strip().upper()[0]
    while r not in 'SN':
        r = str(input('Deseja cadastrar mais uma pessoa? [S/N]')).strip().upper()[0]
    if r != 'S':
        break
print(f'{i} pessoas já atingiram a maioridade.')
print(f'{homem} homens foram cadastrados e {mulher} mulheres tem menos de 20 anos.')
print(f'{mulher} mulheres e {homem} homens.')