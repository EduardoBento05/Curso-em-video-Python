#Exercício Python 37: Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.
n = int(input('Digite qualquer número inteiro para a conversão:'))
print('''Escolha uma das bases para conversão: 
[1] para binário 
[2] para octal 
[3] para hexadecimal''')
escolha = int(input('Sua escolha é: '))
if escolha == 1:
    print('{} convertido para binário é igual a {}'.format(n, bin(n)[2:]))
elif escolha == 2:
    print('{} convertido para octal é igual a {}'.format(n,oct(n)[2:])) 
elif escolha == 3:
    print('{} convertido para hexadecimal é igual a {}'.format(n,hex(n)[2:]))
else:
    print('Opção inválida.Tente novamente.')
    #erreisófaltousaberconverter