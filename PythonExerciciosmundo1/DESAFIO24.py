#Exercício Python 24: Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.

n = str(input('Digite um nome de uma Cidade:')).strip()
lista = n.upper().split()
verificar = 'SANTO' in lista [0]
print(verificar)
#Correto