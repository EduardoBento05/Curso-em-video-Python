#Exercício Python 67: Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo. 
n = 0
while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    if n > 0:
           for c in range(1,11):
               print(f'{n} x {c} = {n*c}')
    if n < 0:
        break
print('PROGRAMA TABUADA ENCERRADO.')
#correto