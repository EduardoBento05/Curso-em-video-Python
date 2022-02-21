#Exercício Python 060: Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo:
#5! = 5 x 4 x 3 x 2 x 1 = 120
from math import factorial
print('Digite um número para')
n = int(input('Calcular seu fatorial: '))
c = n
print('Calculando {}! = '.format(n),end='')
while c > 0:
    Calcular = factorial(n)
    print('{}'.format(c), end='')
    print(' x 'if c > 1 else ' = ', end='')
    c -= 1 
print('{}'.format(Calcular))
#correto