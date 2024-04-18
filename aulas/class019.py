'''pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
print(pessoas['nome'])
print(pessoas['sexo'])
print(pessoas['idade'])
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
del pessoas['sexo']
pessoas['nome'] = 'Leandro'
pessoas['sexo'] = 'M'
pessoas['peso'] = 98.5
for k,v in pessoas.items():
    print(f'{k} = {v}')'''

'''brasil = []
estado1 = {'uf': 'Rio de Janeiro','sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)

print(brasil[0])
print(brasil[1])
print(brasil[0]['uf'])
print(brasil[0]['sigla'])
print(brasil[1]['uf'])
print(brasil[1]['sigla'])'''

estado = dict()
brasil= list()
for c in range(0, 3):
    estado['uf'] = str(input('Universidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
for e in brasil:
    for k, v in  e.items():
        print(f'O campo {k} tem valor {v}.')
print(brasil)

