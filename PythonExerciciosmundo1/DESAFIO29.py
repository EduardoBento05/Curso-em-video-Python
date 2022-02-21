#Exercício Python 29: Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.
v = float(input('Qual é a velocidade do carro?'))
if v > 80:
    print('VOCÊ FOI MULTADO.E O VALOR DA MULTA É = R${}'.format((v-80)*7))
else:
    print('VOCÊ ESTÁ DIRIGINDO COM RESPONSABILIDADE!!PARABÉNSS!!')    
    #correto