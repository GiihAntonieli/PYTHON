celso = float(input('informe a temperatura em ºC: '))
f = celso * 1.8 + 32
fah = (( 9 * celso ) / 5) + 32
print('A temperatura {:.1f}ºC equivale a {:.1f}ºF e {:.1f}ºF' .format(celso, f, fah))
