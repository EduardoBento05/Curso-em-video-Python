#Exercício Python 22: Crie um programa que leia o nome completo de uma pessoa e mostre:
#– O nome com todas as letras maiúsculas e minúsculas.
#– Quantas letras ao todo (sem considerar espaços).
#– Quantas letras tem o primeiro nome.#

nome = str(input('Digite o seu nome inteiro:')).strip()
m1 = nome.upper()
m2 = nome.lower()
letras = (len(nome) - nome.count(' '))
separa = nome.split()

print('Seu nome em maiuscula é {}'.format(m1))
print('Seu nome em minuscula é {}'.format(m2))
print('Seu nome tem ao todo {} Letras'.format(letras))
print('O seu primeiro nome é {} e ele tem {} Letras'.format(separa[0],len(separa[0])))
#quaseCerto o mais dificil foi saber quantas letras tem o primeiro nome