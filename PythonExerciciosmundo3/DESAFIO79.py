#Exercício Python 079: Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
valores = [ ]
deseja = ' '
while True:
    n = int(input('Digite um número: '))
    if n not in valores:
        valores.append(n)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado!Não vou adicionar...')
    deseja = str(input('Deseja continuar [S/N]? ')).upper().strip()
    if deseja in 'Nn':
        break
valores.sort()
print(f'Lista = {valores}')
#correto


