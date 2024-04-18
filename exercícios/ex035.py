r1 = float(input('Digite um valor: '))
r2 = float(input('Digite um outro valor: '))
r3 = float(input('Digite um terceiro valor: '))

#Verificar quem é o maior
maior = r1
if r2 > r1 and r2 > r3:
    maior = r2
if r3 > r1 and r3 > r2:
    maior = r3

#verificar quais são os menores
menor1 = r1
if r2 < r1 and r2 < r3:
    menor1 = r2
if r3 < r1 and r3 < r2:
    menor1 = r3

menor2 = r1
if r2 < r1 and r2 < r3:
    menor2 = r2
if r3 < r1 and r3 < r2:
    menor2 = r3

#fazera conta
soma = menor1 + menor2
if soma > maior:
    print('É POSSÍVEL haver um triângulo!')
else:
    print('NÃO É POSSÍVEL existir um triângulo!')

'''
r1 = float(input('Digite um valor: '))
r2 = float(input('Digite um outro valor: '))
r3 = float(input('Digite um terceiro valor: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
   print('É possível haver um triângulo!')
else:
    print('Não é possível existir um triângulo!')
'''

