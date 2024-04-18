''''\033[0; 30; 41m
print('algo')
\033[4; 33;44m
\033[1; 35; 43m
\033[30; 42m
\033[m
\033[7;30m'''
'''
print('\033[7;33;44mOlá, mundo!\033[m')'''
'''
a = 3
b = 5
print('Os valores são \033[32m{}\033[m e \033[31m{}\033[m!!!' .format(a, b))'''
'''
nome = 'Giovanna'
cores = {'limpa' : '\033[m', 
         'azul' : '\033´[34m',
         'amarelo' : '\033[33m',
         'pretobranco' : '\033[7;30m'}
print('Olá ! Muito prazer em te conhecer, {}{}{}!!'.format('\033[4;34m', nome, '\033[m'))'''

nome = 'Giovanna'
cores = {'limpa' : '\033[m',
         'azul' : '\033´[34m',
         'amarelo' : '\033[33m',
         'pretobranco' : '\033[7;30m'}
print('Olá ! Muito prazer em te conhecer, {}{}{}!!'.format(cores['pretobranco'], nome, cores['limpa']))

