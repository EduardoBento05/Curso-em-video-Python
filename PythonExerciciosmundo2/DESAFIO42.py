#Exercício Python 42: Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
#– EQUILÁTERO: todos os lados iguais
#– ISÓSCELES: dois lados iguais, um diferente
#– ESCALENO: todos os lados diferentes 

a = float(input('Digite o valor do primeiro segmento:'))
b = float(input('Digite o valor do segundo segmento:'))
c = float(input('Digite o valor do terceiro segmento:'))
soma1 = (a+b)
soma2 = (a+c)
soma3 = (b+c)
if soma1 > c and soma2 > b and soma3 > a:
    print('É possivel fomar um triangulo!!')
    if a == b == c:
     print('EQUILÁTERO') 
    if a != b != c != a:
     print('ESCALENO')
    else:
     print('ISÓSCELES')
else:
    print('Não é possivel formar um triangulo!!')
    #correto