#Exercício Python 038: Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
#– O primeiro valor é maior
#– O segundo valor é maior
#– Não existe valor maior, os dois são iguais
n1 = int(input('Digite o primeiro número:'))
n2 = int(input('Digite o segundo número:'))
if n1 > n2:
    print('O primeiro valor {} é maior que o segundo valor {}'.format(n1,n2))
elif n1==n2:
    print('O primeiro valor {} é igual ao segundo valor {}'.format(n1,n2))
else:
    print('O segundo valor {} é maior que o primeiro valor {}'.format(n2,n1))
    #correto
    