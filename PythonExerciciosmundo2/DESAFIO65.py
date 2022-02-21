#Exercício Python 65: Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
from time import sleep
n = 0 
cont = 0 
media = 0
maior = 0 
menor = 0
soma = 0
q = 'S'
while q in 'Ss':
    n = float(input('Digite um número: '))
    soma = soma + n 
    cont += 1
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    q = str(input('Quer continuar? [S/N]')).upper()
media = soma / cont       
print('Você digitou {} números e  média foi igual a {:.2f}'.format(n,media))
print('O maior valor é igual {} e o menor valor é igual a {}'.format(maior,menor))
#correto