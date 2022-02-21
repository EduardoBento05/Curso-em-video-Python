#Exercício Python 34: Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.
s = float(input('Qual é valor do salário do funcionário:'))
if s > 1250:
    print('O seu aumento salarial será igual a {:.2f}'.format(s*1.1))
else:
    print('O seu aumento salarial será igual a {:.2f}'.format(s*1.15))   
