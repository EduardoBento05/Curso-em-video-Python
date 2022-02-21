#Exercício Python 080: Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.
valores = [ ]
for cont in range (0,5):
    n = int(input('Digite um valor: '))      
    if cont == 0 or n > valores[-1] :
        valores.append(n)
        print('Valor adicionado no final da lista...')
    else:
        pos = 0
        while pos < len(valores):
            if n <= valores[pos]:
                valores.insert(pos,n)
                print(f'Valor adicionado na posição {pos} da lista...')
                break
            pos += 1
print(f'Lista: {valores}')
#errei