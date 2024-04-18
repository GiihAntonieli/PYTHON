'''cidade = str(input('digite o nome de uma cidade: ')).split()
cidade = 'santo' in cidade
print(cidade)'''

cidade = str(input('digite o nome de uma cidade: ')).strip()
cidade = cidade[:5].upper() == 'SANTO'
print(cidade)
