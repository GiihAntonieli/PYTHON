n1 = int(input("Um valor: "))
n2 = int(input('outro valor: '))
s = n1+n2
m = n1*n2
d = n1/n2
di = n1//n2
div = n1%n2
e = n1**n2
print('A soma é {}, o produto {} é tanto e a divisão é {:.3f}' .format(s,m,d), end=' >>> ')
print('divisão inteira {} e potência {}' .format(di,e))