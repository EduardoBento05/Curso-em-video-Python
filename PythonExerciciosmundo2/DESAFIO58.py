#Exercício Python 58: Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
from random import randint
tentativas = 0
print('Sou o seu computador!')
print('Vou pensar em um número entre 0 a 10.Tente advinhar..')
n = int(input('Em que número eu pensei?: '))
while randint(0,10) != n:
    tentativas += 1
    print('Você errou , tente mais uma vez...')
    n = int(input('Qual é o seu palpite?: '))
print('Após {} tentativas , Você finalmente acertou!!'.format(tentativas))
#correto

