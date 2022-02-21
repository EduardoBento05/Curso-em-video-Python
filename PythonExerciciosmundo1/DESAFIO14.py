#Exercício Python 14: Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.
c = float(input('Digite Uma temperatura em Graus Celsius:'))
print('A sua temperatura em {:.2f}°C convertida é = {:.2f}°F'.format(c,(1.8*c)+32))
#correto