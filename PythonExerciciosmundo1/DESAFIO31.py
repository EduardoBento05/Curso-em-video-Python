#Exercício Python 31: Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 para viagens mais longas.
d = float(input('Qual a distancia da sua viagem em km?'))
if d <= 200:
    p1 = d*0.5
    print('O Preço da passagem para viagens curtas é igual a R${}'.format(p1))
else:
    p2 = d*0.45
    print('O preço da passagem para viagens longas é igual a R${}'.format(p2))    
    #correto