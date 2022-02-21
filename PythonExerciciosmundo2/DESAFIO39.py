    #Exercício Python 39: Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
a = int(input('Qual é o ano que você nasceu?:'))
idade = 2020 - a
alistar = idade - 18
alistamento = 2020 - alistar
if idade > 18:
    print('''
    Quem nasceu em {} tem {} anos em 2020
    você deveria ter se alistado há {} anos
    seu alistamento foi em {}'''.format(a,idade,alistar,alistamento))
elif idade == 18:
    print('Você tem que se alistar imediatamente!')
else:
    print('faltam {} anos para o seu alistamento'.format(alistar*(-1)))
    #correto