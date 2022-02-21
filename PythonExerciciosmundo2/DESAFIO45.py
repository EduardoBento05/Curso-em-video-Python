#Exercício Python 45: Crie um programa que faça o computador jogar Jokenpô com você.
from random import randint
from time import sleep
itens = ('PEDRA','PAPEL','TESOURA')
computador = randint(0,2)
print(''' ESCOLHA UMA DAS OPÇÕES:
[0]PEDRA
[1]PAPEL
[2]TESOURA ''')
escolha = int(input('Escolha sua jogada é :'))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
sleep(1)
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[escolha]))
if computador == 0: #computador jogou pedra
    if escolha == 0:
        print('EMPATE')
    elif escolha == 1:
        print('JOGADOR VENCE')
    elif escolha == 2:
         print('COMPUTADOR VENCE')
    else:
        print('JOGADA INVÁLIDA')
elif computador == 1: #computador jogou papel
    if escolha == 0:
        print('COMPUTADOR VENCE')
    elif escolha == 1:
        print('EMPATE')
    elif escolha ==2:
        print('JOGADOR VENCE')
    else:
        print('JOGADA INVÁLIDA')
elif computador == 2 : #computador jogou tesoura
    if escolha == 0:
        print('JOGADOR VENCE')
    elif escolha == 1:
        print('COMPUTADOR VENCE')
    elif escolha ==2:
         print('EMPATE')
    else:
        print('JOGADA INVÁLIDA')
        #errei mas  tive noção do que fazer
     