'''frase = str(input('Digite um frase: '))
letra = frase.count('a')
posicao = frase.find('a')
print('{} possui {} letras (a), ela está nas posições {} ' .format(frase, letra, posicao))'''
frase = str(input('Digite um frase: ')).upper().strip()
print('a letra A aparece {} vezes na frase.' .format(frase.count('A')))
print('A primeira letra A aparece na posição {}' .format(frase.find('A')+1))
print('A última letra A aparece na posição {}' .format(frase.rfind('A')+1))

