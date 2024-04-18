from math import pow,sqrt,hypot
co = float(input('Digite o cateto oposto: '))
ca = float(input('Digite o cateto adjascente: '))
pot = pow(co, 2) + pow(ca, 2)
hi = sqrt(pot)
print('O comprimento da Hipotenusa é de {:.2f}' .format(hi))

'''
co = float(input('Digite o cateto oposto: '))
ca = float(input('Digite o cateto adjascente: '))
hi = hypot(co,ca)
print('O comprimento da Hipotenusa é de {:.2f}' .format(hi))'''
