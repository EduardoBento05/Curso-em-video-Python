#Exercício Python 041: A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
#– Até 9 anos: MIRIM
#– Até 14 anos: INFANTIL
#– Até 19 anos: JÚNIOR
#– Até 25 anos: SÊNIOR
#– Acima de 25 anos: MASTER
a = int(input('Em que ano você nasceu?:'))
idade = 2020 - a
if idade <= 9:
    print('SUA IDADE É IGUAL A {} E VOCÊ PERTENCE A CATEGORIA MIRIM'.format(idade))
elif idade <= 14:
    print('SUA IDADE É IGUAL A {} E VOCÊ PERTENCE A CATEGORIA INFANTIL'.format(idade))
elif  idade <= 19 :
    print('SUA IDADE É IGUAL A {} E VOCÊ PERTENCE A CATEGORIA JUNIOR'.format(idade))
elif  idade <= 25:
    print('SUA IDADE É IGUAL A {} E VOCÊ PERTENCE A CATERGORIA SENIOR'.format(idade)) 
else :
    print('SUA IDADE É IGUAL A {} E VOCÊ PERTENCE A CATERGORIA MASTER'.format(idade))
    #correto
    
    