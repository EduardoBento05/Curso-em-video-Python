#Exercício Python 27: Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente. 
nome = str(input('Qual é o seu nome completo?')).upper().strip().split()
print('O primeiro nome é {}'.format(nome[0]))
print('O ultimo nome é igual {}'.format(nome[-1]))
#Correto