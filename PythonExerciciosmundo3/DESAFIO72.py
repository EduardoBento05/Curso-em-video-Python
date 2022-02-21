#Exercício Python 72: Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

while True:
    n= int(input('Digite um número entre 0 a 20: '))
    if n >= 0 and n <= 20:
        extenso = ('ZERO','UM','DOIS','TRÊS','QUATRO','CINCO','SEIS','SETE','OITO','NOVE','DEZ','ONZE','DOZE','TREZE','CATORZE','QUINZE','DEZESSEIS','DEZESSETE','DEZOITO','DEZENOVE','VINTE') 
        print(f'Você Digitou o número {extenso[n]}')
        break
    else:
        print('Tente Novamente. ', end ='')
        
#correto

    



    