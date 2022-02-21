#Exercício Python 076: Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.

listagem = ('Lápis',1.75,
'Borracha',2,
'Caderno',16,
'Estojo',25,
'Transferidor',4.20,
'Compasso',9.99,
'Mochila',120.25,
'Canetas',22.5)
print('-' * 40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-' * 40)
for item in range(0,len(listagem)):
    if item % 2 == 0:
        print(f'{listagem[item]:.<30}', end= ' ')
    else:
        print(f'R${listagem[item]:>7.2f}')
print('-' * 40)
#correto