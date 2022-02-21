#Exercício Python 51: Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.
pa = 0
p = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a sua razão: '))
décimo = p + (10-1) * r
for c in range(p,décimo+r,r):
    print('{} '.format(c), end = '->')
print('ACABOU')
#errei