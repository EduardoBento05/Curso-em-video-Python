#Exercício Python 16: Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
from math import trunc
n = float(input("Digite um Número Real qualquer: "))
print ('O número digitado foi {} e a sua porção inteira é {}'.format(n,trunc(n)))
#correto