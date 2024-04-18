'''pessoa = dict()
pessoa['nome'] = str(input('Nome: '))
pessoa['ano'] = int(input('Ano de nascimento: '))
pessoa['idade'] = 2018 - pessoa['ano']
pessoa['ctps'] = int(input('Carteira de Trabalho(0 se não tem): '))

if pessoa['ctps'] > 0:
    pessoa['ano de contratação'] = int(input('Ano de Contratação: '))
    pessoa['salário'] = float(input('Salário: '))
    pessoa['aposentadoria'] = pessoa['ano de contratação'] + 35 - pessoa['ano']

print('-='*40)
for k, v in pessoa.items():
    print(f'  - {k} tem o valor {v}')'''


#RESPOSTA
from datetime import datetime
pessoa = dict()
pessoa['nome'] = str(input('Nome: '))
nasc = int(input('Ano de nascimento: '))
pessoa['idade'] = datetime.now().year - nasc
pessoa['ctps'] = int(input('Carteira de Trabalho(0 se não tem): '))
if pessoa['ctps'] != 0:
    pessoa['ano de contratação'] = int(input('Ano de Contratação: '))
    pessoa['salário'] = float(input('Salário: R$'))
    pessoa['aposentadoria'] = (pessoa['ano de contratação'] + 35) - datetime.now().year
print('-='*30)
for k, v in pessoa.items():
    print(f'  - {k} tem o valor {v}')