#Exercício Python 20: O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
from random import shuffle
a1 = str(input('Digite o nome do Primeiro Aluno: '))
a2 = str(input('Digite o nome do Segundo Aluno: '))
a3 = str(input('Digite o nome do Terceiro Aluno: '))
a4 = str(input('Digite o nome do Quarto Aluno: '))
alunos  = [a1,a2,a3,a4]
shuffle(alunos)
print('A Ordem de Apresentação é  {}'.format(alunos))
#errouporpouco faltou acertar o shuffle só