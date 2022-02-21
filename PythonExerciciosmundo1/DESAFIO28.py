#Exercício Python 28: Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.
from random import randint
from time import sleep
print('Vou pensar em um número entre 0 e 5.Tente adivinhar...')
n = int(input('Em que número eu pensei?'))
print('PROCESSANDO...')
sleep(3)
if randint(0,5) == n:
    print('PARABÉNS!!VOCÊ GANHOU!!!')
else:
    print('VOCÊ PERDEU!!!QUE PENA,TENTE NOVAMENTE.')
#correto
