#Exercício Python 18: Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo. 
from math import tan,sin,cos
n = float(input('Digite um angulo qualquer: '))
s = sin(n)
t = tan(n)
c = cos(n)
print('O angulo escolhido foi {}'.format(n))
print('O seu Seno é = {}'.format(s))
print('O seu Cosseno é = {}'.format(c))
print('A sua tangente é = {}'.format(t))
#Correto