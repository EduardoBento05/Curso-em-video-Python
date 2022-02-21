#Exercício Python 11: Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.
l = float(input('Digite a Largura da parede:'))
h = float(input('Digite a Altura da parede:'))
print('A sua area é = {}m²'.format(l*h))
print('E a tinta necessária para pintá-la é = {}L'.format((l*h)/2))
#correto