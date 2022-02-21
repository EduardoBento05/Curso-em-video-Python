#Exercício Python 54: Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
from datetime import date
atual = date.today().year
countmaior = 0
countmenor = 0
for p in range(1,8):
    nasc = int(input('Em que ano a {}ª pessoa nasceu? '.format(p)))
    idade = atual - nasc
    if idade >= 21:
        countmaior += 1
    else:
        countmenor += 1
print('Ao todo tivemos {} pessoas maiores de idade'.format(countmaior))
print('E também tivemos {} pessoas menos de idade'.format(countmenor))
#acertei
       
