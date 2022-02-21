#Exercício Python 12: Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
p = float(input('Digite o preço de um produto:R$'))
print('Preço atual = R${:.2f}.E com Desconto de 5% é = R${:.2f}'.format(p,p*0.95))
#Correto
