#Exercício Python 32: Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
a = int(input('Digite um Ano: '))
bissexto = a%4
if bissexto == 0:
    print('O ano de {} é um ano bissexto'.format(a))
else:
    print('O ano de {} não é um ano bissexto'.format(a))
    #correto