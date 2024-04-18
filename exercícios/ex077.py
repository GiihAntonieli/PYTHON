palavras = ('APRENDER',
            'PROGRAMAR',
            'LINGUAGEM',
            'PYTHON',
            'CURSO',
            'GRATIS',
            'ESTUDAR',
            'PRATICAR',
            'TRABALHAR',
            'MERCADO',
            'PROGRAMADOR',
            'FUTURO')
for pos in range(0, len(palavras)):
    print(f'\nNa palavra {palavras[pos]} temos ', end='')

    if palavras[pos] in 'aeiou':
        letra = palavras[pos]
        print(letra, end='')
        #if letra.lower() in 'aeiou':
            #print(letra, end='')
