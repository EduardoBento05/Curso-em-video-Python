#Exercício Python 62: Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos. 
p = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))
termo = p
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} -> '.format(termo),end='')
        termo += r
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos a mais voce quer mostrar? '))
print('Progressão aritimética finalizada com {} termos mostrados.'.format(total))
#correto