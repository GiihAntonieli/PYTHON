frase = str(input('Digite uma frase: ')).strip().upper()
pali = frase.split()
junto = ''.join(pali)
inverso = '' '''junto[::-1]'''

for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
print(junto, inverso)
if inverso == junto:
    print('Essa frase é um palíndromo!')
else:
    print('Infelizmente essa frase não é um palíndromo!')
















