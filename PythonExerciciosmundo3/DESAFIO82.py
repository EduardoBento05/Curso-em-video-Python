#Exercício Python 082: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.
lista = list()
par = []
impar = []
deseja = ''
while True:
    n = int(input('Digite um valor: '))
    if n not in lista:
        lista.append(n)
        print('Numero adicionado com sucesso...')
    else:
        print('->'*30)
    deseja = str(input('Deseja continuar [S/N]?')).upper().strip()
    if deseja in 'Nn':
        break
lista.sort()
print(f'Lista original = {lista}')
for valor in lista:
    if valor % 2 == 0:
        par.append(valor)
    else:
        impar.append(valor)
par.sort()
impar.sort()
print(f'A lista par é igual {par}')
print(f'A lista impar é igual {impar}')
#correto


