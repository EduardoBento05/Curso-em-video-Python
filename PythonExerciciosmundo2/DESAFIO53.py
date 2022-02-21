#Exercício Python 53: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços. Exemplos de palíndromos:APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.
f = str(input('Escreva uma Frase: ')).upper().strip()
d = f.split()
j = ''.join(d)
i = ''
for l in range(len(j) - 1,-1,-1):
    i += j[l]
if i == j:
    print('TEMOS UM PAlÍNDROMO!')
else:
    print('NÃO É UM PALÍNDROMO!')
#errei