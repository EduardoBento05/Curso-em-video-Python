#Exercício Python 36: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
from time import sleep
c = float(input('Qual é o valor da casa? R$'))
s = float(input('Qual é o valor do seu salário? R$'))
a = int(input('Quantos anos de financiamento?'))
prestação = c / (a*12)
verificar = s*0.3
if prestação <= verificar:
    print('EMPRÉSTIMO APROVADO!')
    sleep(3) 
    print('O valor da casa é igual R${} e sua parcela será R${} em {} anos '.format(c,prestação,a))
     
else:
    print('EMPRÉSTIMO REPROVADO')
    sleep(3)
    print('Para pagar uma casa de R${} em {} anos é necessário uma prestação de R${:.2f}'.format(c,a,prestação))
    #correto