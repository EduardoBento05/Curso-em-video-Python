#Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas,guardando tudo em uma lista. No final, mostre:A) Quantas pessoas foram cadastradas.                                                                                                   B) Uma listagem com as pessoas mais pesadas.                                                                                                    C) Uma listagem com as pessoas mais leves.

pessoas = list()
dados = list()
peso = list()
while True:
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Peso: ')))
    pessoas.append(dados[:])
    peso.append(dados[1])
    dados.clear()
    resp = str(input('Deseja continuar [S/N]')).upper().strip()
    if resp in 'Nn':
        break
print(f'Você cadastrou {len(pessoas)}pessoas.')
print(f'A pessoa mais pesada pesa {max(peso):.2f}kg.',end='')
for p in pessoas:
    if p[1] == max(peso):
        print(f'{p[0]}',end= '')
    print(f'\n O menor peso foi de {min(peso):.2f}kg.',end='')
for p in pessoas:
    if p[1]==min(peso):
        print(f'{p[0]}',end='')
#correto

        
        
