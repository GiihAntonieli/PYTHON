'''ano = int(input('Ano de nascimento: '))

alistamento = 2023 - ano

if alistamento == 18:
    print('Você deve se alistar IMEDIATAMENTE pois, você possui {}' .format(alistamento))
elif alistamento > 18:
    print('Você PASSOU do tempo de se alistar pois, possui {}.' .format(alistamento))
else:
    print('Você AINDA não pode se alistar pois, possui {}' .format(alistamento))'''

from datetime import date
atual = date.today().year
nasc = int(input('Ano de nascimento: '))
idade = atual - nasc
print('Quem nasceu em {} tem {} anos em {}.' .format(nasc, idade, atual))

if idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')
elif idade < 18:
    saldo = 18 - idade
    print('Você ainda não tem 18 anos falta {} para o alistamento' .format(saldo))
    ano = atual + saldo
    print('Seu alistamento será em {}' .format(ano))
elif idade > 18:
    saldo = idade - 18
    print('Você já deveria ter se alistado há {} anos' .format(saldo))
    ano = atual - saldo
    print('Seu alistamento foi em {}' .format(ano))


