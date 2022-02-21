#Exercício Python 46: Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.
from time import sleep
for c in range (10,0-1,-1):
    print('COMEÇOU A CONTAGEM RECRESSIVA PARA O ESTOURO DOS FOGOS DE ARTIFICIOS {}'.format(c))
    sleep(1)
print('FELIZ ANO NOVO!!')
#correto