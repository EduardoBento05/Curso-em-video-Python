#Exercício Python 13: Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento
s = float(input('Digite o salário de um funcionário:R$'))
print('O salário atual é = R${:.2f},e seu salário com aumento é = R${:.2f}'.format(s,s*1.15))
#correto