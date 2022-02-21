#Exercício Python 35: Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
a = float(input('Digite o valor do primeiro segmento:'))
b = float(input('Digite o valor do segundo segmento:'))
c = float(input('Digite o valor do terceiro segmento:'))
soma1 = (a+b)
soma2 = (a+c)
soma3 = (b+c)
if soma1 > c and soma2 > b and soma3 > a:
    print('É possivel fomar um triangulo!!')
else:
    print('Não é possivel formar um triangulo!!')
    #correto