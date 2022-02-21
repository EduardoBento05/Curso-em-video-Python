#Exercício Python 081: Crie um programa que vai ler vários números e colocar em uma lista.                  Depois disso, mostre:                                                                                                       A) Quantos números foram digitados.                                                                                                 
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.  

lista = [ ]
deseja = ' '
digitados = 0
while True:
    n = int(input('Digite um valor: '))
    digitados += 1
    if n not in lista:
        lista.append(n)
        print('Valor adicionado com sucesso...')
    else:
        print('^-30')
    deseja = str(input('Deseja continuar [S/N]? ')).upper().strip()
    if deseja in 'Nn':
        break
lista.sort(reverse=True)
print(f'Foram digitados {digitados} números.')
print(f'Lista decrescente = {lista}')
if  5 in lista:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não faz parte da lista!')
    #correto

    