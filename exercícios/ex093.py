#LISTAS
futebol = dict()
jogos = list()

#NOME JOGADOR
futebol['nome'] = str(input('Qual o nome do jogador: '))

#GOLS DAS PARTIDAS
partidas = int(input(f'Quantoas partidas {futebol["nome"]} jogou: '))
for c in range(1, partidas+1):
    jogos.append(int(input(f'Quantos gols na partida {c}: ')))
    futebol['gols'] = jogos
futebol['total'] = 0

#SOMATÓRIA DOS GOLS
for i in jogos:
    futebol['total'] += i
print('-='*40)
print(futebol)
print('-='*40)

#RESULTADO
for k, v in futebol.items():
    print(f'O campo {k} tem o valor {v}.')
print('-='*40)

#RECAPÍTULANDO OS JOGOS
print(f'O jogador {futebol["nome"]} jogou {c} partidas.')
for k, v in enumerate(jogos):
    print(f'  => Na partida {k}, fez {v} gols.')
print(f'Foi um total de {futebol["total"]} gols.')



