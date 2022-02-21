#Exercício Python 70: Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
#A) qual é o total gasto na compra.
#B) quantos produtos custam mais de R$1000.
#C) qual é o nome do produto mais barato. 

totalgasto = custammais = barato = cont =  0
barato2 = ''
while True:
    produto = str(input('Nome do Produto: ')).upper().strip()
    preço = float(input('Preço:R$ '))
    cont += 1
    totalgasto = totalgasto + preço
    if preço > 1000:
        custammais += 1
    if cont == 1 or preço < barato:
        barato = preço
        barato2 = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer Continuar? [S/N]')).strip().upper()[0]
    if resp == 'N':
        break
print(f'O total da compra foi de R$ {totalgasto}')
print(f'Temos {custammais} Produto(s) custando mais de R$1000.00 ')
print(f'O produto mais barato foi (a/o) {barato2} que custa R${barato:.2f}')
#correto

