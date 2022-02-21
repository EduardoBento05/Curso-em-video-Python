#Exercício Python 44: Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
#– à vista dinheiro/cheque: 10% de desconto
#– à vista no cartão: 5% de desconto
#– em até 2x no cartão: preço formal 
#– 3x ou mais no cartão: 20% de juros
p = int(input('Qual é o valor da sua compra?R$'))
print(''' FORMAS DE PAGAMENTO:
   [1] à vista dinheiro/cheque
   [2] à vista no cartão
   [3] em até 2x no cartão
   [4] 3x ou mais no cartão ''')
escolha = int(input('Sua escolha é :'))
if escolha == 1:
    print('Sua compra de R${} vai custar R${} '.format(p,p*0.9))
elif escolha == 2:
    print('Sua compra de R${} vai custar R${}' .format(p,p*0.95))
elif escolha == 3:
    parcelas = p/2
    print('Sua compra de R${} vai custar duas parcelas de R${}'.format(p,parcelas))
elif escolha == 4:
    p1 = int(input('Quantas Parcelas?:'))
    parcelas1 = p/p1+(p/p1)*0.2
    n = p+p*0.2
    print(''' Sua compra será parcelada em {}x de {} com juros
    Sua compra de R${} vai custar R${} no final.'''.format(p1,parcelas1,p,n))
    #correto