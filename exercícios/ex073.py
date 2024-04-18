brasileirao = ('Botafogo', 'Palmeiras', 'Grêmio',
               'Flamengo','Fluminense','Bragantino',
               'Athletico-PR','Fortaleza','Atlético-MG',
               'Cuiabá','São Paulo','Cruzeiro','Corinthians',
               'Internacional','Goiás','Bahia','Santos','Vasco',
               'América-MG','Coritiba')
print('-=' * 15)
print(f'Os 5 primeiros são {brasileirao[0:5]}' )
print('-=' * 15)
print(f'os 4 últimos são {brasileirao[15:]}' )
print('-=' * 15)
print(f'Times em ordem alfabética {sorted(brasileirao)}')
print('-=' * 15)
print(f'O Corinthians está na {brasileirao.index("Corinthians")} posição')