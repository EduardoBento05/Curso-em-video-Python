#Exercício Python 19: Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.
#import random
#alunos = 'Joao','José','Pedro','Eduardo'
#sorteio = random.choices(alunos)
#print('O aluno Escolhido para apagar o quadro foi o {}'.format(sorteio))#primeira solução correta
from random import choice
a = str(input('Digite o nome do Primeiro Aluno: '))
a1 = str(input('Digite o nome do Segundo Aluno: '))
a2 = str(input('Digite o nome do Terceiro Aluno: '))
a3 = str(input('Digite o nome do Quarto Aluno: '))
alunos = [a,a1,a2,a3]
escolhido = choice(alunos)
print('O aluno escolhido para apagar o quadro foi o/a {}'.format(escolhido))
#correto