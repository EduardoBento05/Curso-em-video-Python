#Exercício Python 26: Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”, em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.
n = str(input('Digite uma Frase:')).strip().upper()
print('A letra A aparece {}'.format(n.count('A')))
print('O primeiro A Fica na posição {}'.format(n.find('A')+1))
print('O segundo A Fica na posição {}'.format(n.rfind('A')+1))
#correto