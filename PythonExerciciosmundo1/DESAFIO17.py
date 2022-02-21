#Exercício Python 17: Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.
from math import hypot
n = float(input('Qual é o valor do cateto oposto do Triangulo Retangulo?:'))
n1 = float(input('Qual é o valor do cateto adjacente do Triangulo Retangulo?:'))
h = hypot(n,n1)
print('Os catetos medem {} e {} , e sua hipotenusa é igual a {}'.format(n,n1,h))
#Correto