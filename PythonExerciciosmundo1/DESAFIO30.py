#Exercício Python 30: Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.
n = int(input('Digite um número:'))
verificar = n%2
if verificar == 0:
    print('O numero {} é par'.format(n))
else:
    print('O numero {} é impar'.format(n))
    #correto