#Exercício Python 25: Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.
n = str(input('Digite o seu nome inteiro:')).strip()
lista = n.upper()
verificar = 'SILVA' in lista 
print('Seu nome tem Silva? {}'.format(verificar))