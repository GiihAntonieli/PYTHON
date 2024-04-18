'''
    tempo = int(input("Quantos anos tem seu carro? "))
        if tempo <=3:
            print("carro novo")
        else:
            print("carro velho")
        print("--FIM--")
'''
'''
    tempo = int(input("Quantos anos tem seu carro? "))
    print("carro novo" if tempo <=3 else "carro velho")
    print("--FIM--")'''
'''nome = str(input('Qual é o seu nome? '))
if  nome == 'Gustavo':
    print( 'Que nome lindo você tem!')
else:
    print('Seu nome é tão normal!')
print('Bom dia , {}!' .format(nome))'''
n1 =float(input("digite a primeira nota: "))
n2 = float(input("digite a segunda nota: "))
m = (n1+n2)/2
print("A sua média foi {:.1f}" .format(m))
if m >= 6:
    print("Aprovado(a)!!!")
else:
    print("Reprovado(a)!")

