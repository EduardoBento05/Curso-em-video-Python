#Exercício Python 077: Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
listagem = ('APRENDER','AMAR','ESTUDAR','EDUCAR','PRATICAR','FUTURO','PROGRAMADOR')

for c in listagem:
    print(f'\nNa palavra {c.upper()} temos ', end='')
    for letra in c:
        if letra.lower() in 'aeiou':
            print(letra,end=' ')
            #correto