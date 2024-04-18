from math import sin, cos, tan, radians
ang = float(input("Digite um ângulo: "))
a = radians(ang)
s = sin(a)
c = cos(a)
t = tan(a)
print('Este Ângulo de {}º possui o Seno de {:.2f}º, Cosseno de {:.2f}º e Tangente de {:.2f}º' .format(ang, s, c, t))
