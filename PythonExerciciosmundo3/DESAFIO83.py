#Exercício Python 083: Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.
lista = list()
e = str(input('Digite uma expressão qualquer que use parênteses: '))
for valor in e: 
    if valor  == '(':
      lista.append('(')
    elif valor == ')':
        if len(lista)>0:
            lista.pop()
        else:
            lista.append(')')
            break
if len(lista) == 0:
    print('Expressão correta.')
else:
    print('Expressão errada.')
    #errei