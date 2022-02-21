'''Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso. '''
from time import sleep
n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
menu = 0
while menu != 5:
    print('Qual é a sua opção?')
    menu = int(input('''--------MENU---------
    [1]SOMAR
    [2]MULTIPLICAR
    [3]MAIOR
    [4]NOVOS NÚMEROS
    [5]SAIR DO PROGRAMA '''))
    sleep(1)
    if  menu == 1:
        soma = n1 + n2
        print('A soma entre {} e {} é igual {}'.format(n1,n2,soma))
    elif menu == 2:
        multiplicar = n1*n2
        print('A multiplicação entre {} e {} é igual {}'.format(n1,n2,multiplicar))
    elif menu == 3:
        if n1 > n2:
            print('{} é maior que {}'.format(n1,n2))
        else:
            print('{} é maior que {}'.format(n2,n1))
    elif menu == 4:
        n1 = int(input('Digite um novo número: '))
        n2 = int(input('Digite outro novo número: '))
    elif menu == 5:
        print('Finalizando o programa...')
        sleep(3)
    else:
        print('ERROR ---Operação inválida---- ERROR')
print('PROGRAMA FINALIZADO.')
#correto