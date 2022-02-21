#Exercício Python 68: Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo. 
from random import randint
computador = randint (0,10)
s = cont = 0
while True:
    print('VAMOS JOGAR PAR OU ÍMPAR')
    escolha = int(input('Digite um valor: '))
    escolha2 = str(input('Par ou Ímpar? [P/I]')).upper().strip()
    if escolha2 == 'P':
        s = computador + escolha
        if s % 2 == 0 :
            print('VOCÊ GANHOU!')
            print(f'Você jogou {escolha} e o computador jogou {computador}.Total é igual a {s} DEU PAR')
            cont += 1
        else:
            print('VOCÊ PERDEU!')
            print(f'Você jogou {escolha} e o computador jogou {computador}.Total é igual a {s} DEU IMPAR')
            break
    if escolha2 == 'I':
        s = computador + escolha
        if s % 2 !=0:
            print('VOCÊ GANHOU!')
            print(f'Você jogou {escolha} e o computador jogou {computador}.Total é igual a {s} DEU IMPAR')
            cont += 1
        else:
            print('VOCÊ PERDEU!')
            print(f'Você jogou {escolha} e o computador jogou {computador}.Total é igual a {s} DEU PAR')
            break
print(f'GAME OVER!!Você venceu {cont} (vez/vezes)')
#correto