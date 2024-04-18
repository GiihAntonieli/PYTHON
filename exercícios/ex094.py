#CADASTRO NOS DICIONÁRIOS
'''cadastro = dict()
pessoas = list()
mulher = list()
totF = 0
age = 0
while True:
    cadastro['nome'] = str(input('Nome: '))
    #VALIDAÇÃO DO SEXO
    cadastro['sexo'] = str(input('Sexo[M/F]: '))
    while cadastro['sexo'] not in 'MmFf':
        print('Tente novamente! F para FEMININO e M para MASCULINO')
        cadastro['sexo'] = str(input('Sexo[M/F]: '))
    cadastro['idade'] = int(input('Idade: '))
    pessoas.append(cadastro.copy())
   #VALIDAÇÃO PARA CONTINUAR
    resp = str(input('Quer continuar: [S/N] '))
    while resp not in 'SsNn':
        print('Tente novamente! S para SIM e N para NÃO')
        resp = str(input('Quer continuar: [S/N] '))
    if resp in 'Nn':
        break

print('-='*40)
print(pessoas)
for k, v in enumerate(pessoas):
    age += pessoas[k]['idade']
    if pessoas[k]['sexo'] in 'Ff':
        totF += 1
        mulher.append(pessoas[k]['nome'])

age = age / (k+1)
print(f'  A) Ao todo o grupo tem {k+1} pessoas.')
print(f'  B) A média de idade é de {age:.2f} anos.')
print(f'  C) As mulheres cadastradas foram: {mulher}')
print(f'  D) Lista das pessoas que estão acima da média: ')
for p in galera:
    if p["idade"] >= média:
        print('    ', end='')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print('<< ENCERRADO >>')'''


#RESPOSTA
pessoa = dict()
galera = list()
soma = média = 0

while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo[M/F]: ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resp = str(input('Quer continuar: [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp == 'N':
        break
print('-=' *30)
print(f'  A) Ao todo o grupo tem {len(galera)} pessoas.')
média = soma / len(galera)
print(f'  B) A média de idade é de {média:5.2f} anos.')
print(f'  C) As mulheres cadastradas foram: ', end='')
for p in galera:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]} ',end='')
print()
print(f'  D) Lista das pessoas que estão acima da média: ')
for p in galera:
    if p["idade"] >= média:
        print('    ', end='')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print('<< ENCERRADO >>')


