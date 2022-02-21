#Exercício Python 61: Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.
from time import sleep
p = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))
termo = p
menu = 0
count = 1
while menu != 2:
    menu = int(input('''---MENU---
    [1]APERTE 1 PARA SABER OS 10 PRIMEIROS TERMOS DA PA
    [2]APERTE 2 PARA SAIR
    '''))
    if menu == 1:
        while count < 10:
            print('{} ->'.format(termo),end='')
            termo += r
            count += 1    
    elif menu == 2:
        print('FINALIZANDO O PROGRAMA...')
        sleep(3)
print('PROGRAMA FINALIZADO COM SUCESSO!')
#errei