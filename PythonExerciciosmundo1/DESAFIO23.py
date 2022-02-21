#Exercício Python 23: Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

n = float(input('Digite um numero de 0 a 9999:'))
num = str(n)
unindade = num[3] 
dezena = num[2]
centena = num[1]
milhar = num[0]
print('O numero da unindade é igual a {}'.format(unindade))
print('O numero da dezena é igual a {}'.format(dezena))
print('O numero da centena é igual a {}'.format(centena))
print('O numero do milhar é igual a {}'.format(milhar))
#correto