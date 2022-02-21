#Exercício Python 078: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
valores = list()
maior = menor = 0
for cont in range (0,5):
    valores.append(int(input(f'Digite um valor para a posição {cont}: ')))
    print(f'o maior valor é  igual a {max(valores)} nas posições', end=' ')
for i , v in enumerate(valores):
    if v == max(valores):
        print(f'{i}...', end=' ')
print(f'e o menor valor é igual a {min(valores)} nas posições.', end=' ')
for i , v in enumerate(valores):
    if v == min(valores):
        print(f'{i}...', end=' ')
        #correto

    

    