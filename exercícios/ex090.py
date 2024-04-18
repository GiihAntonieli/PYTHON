aluno = dict()
aluno['nome'] = str(input('Nome: '))
aluno['média'] = float(input(f'Média de {aluno["nome"]}: '))
print('-='*40)
for k, v in aluno.items():
    print(f'- {k} é igual a {v}')
if aluno['média'] >= 7:
    print('- Situação é igual a APROVADO!')
else:
    print('Situação é igual a REPROVADO!!!')


#RESPOSTA
'''aluno = dict()
aluno['nome'] = str(input('Nome: '))
aluno['média'] = float(input(f'Média de {aluno["nome"]}: '))

if aluno['média'] >= 7:
    aluno['situação'] = 'APROVADO'
elif 5 <= aluno['média'] < 7:
    aluno['situação'] = 'RECUPERAÇÃO'
else:
    aluno['situação'] = 'REPROVADO'

print('-=' * 40)
for k,v in aluno.items():
    print(f'  - {k} é igual a {v}')'''

