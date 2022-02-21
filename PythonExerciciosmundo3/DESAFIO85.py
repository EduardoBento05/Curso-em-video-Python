#Exercício Python 085: Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.
'''par = list()
impar = list()
for c in range (0,7):
    n = float(input('Digite um número: '))
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)
impar.sort()
par.sort()
print(f'Os valores pares são {par}')
print(f'Os valores impares são {impar}')'''
#correto
valores = [[] , []]
n = 0
for c in range(0,7):
    n = float(input('Digite um número: '))
    if n % 2 == 0:
        valores[0].append(n)
    else:
        valores[1].append(n)
print(f'Os valores pares são {valores[0]}') 
print(f'Os valores impares são{valores[1]}')
#correto
     


    
            