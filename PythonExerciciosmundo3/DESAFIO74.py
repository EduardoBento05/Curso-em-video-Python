#Exercício Python 074: Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.
from random import randint
gerar = (randint(1,10),randint(1,10),randint(1,10),randint(1,10),randint(1,10))
print(f'Os valores sorteados foram {gerar}')
print(f'O Maior valor sorteado foi {max(gerar)}')#comando max mostra o maior valor sorteado de uma tupla
print(f'O menor valor sorteado foi {min(gerar)}')#comando min mostra o menor valor sorteado de uma tupla
#correto