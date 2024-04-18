'''import random
s = random.randint(1, 4)
print("O Aluno sorteado foi o aluno {}" .format(s))'''
import random
n1 = str(input('Digite seu nome: '))
n2 = str(input('Digite seu nome: '))
n3 = str(input('Digite seu nome: '))
n4 = str(input('Digite seu nome: '))
lista = [n1,n2,n3,n4]
escolhido = random.choice(lista)
print('O aluno escolhido foi {}' .format(escolhido))