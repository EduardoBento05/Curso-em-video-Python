#Exercício Python 69: Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
#A) quantas pessoas tem mais de 18 anos.
#B) quantos homens foram cadastrados.
#C) quantas mulheres tem menos de 20 anos. 

'''cadastro =  homens = mulheres = pessoas = idade2 =  0
while True:
    print('CADASTRE UMA PESSOA')
    idade = int(input('Idade: '))
    sexo = str(input('[M/F]')).upper().strip()
    cadastro = str(input('QUER CONTINUAR? [S/N]')).upper().strip()
if cadastro == 'S':
    idade = int(input('Idade: '))
    sexo = str(input('[M/F]')).upper().strip()
    cadastro = str(input('QUER CONTINUAR? [S/N]')).upper().strip()
    if sexo == 'M':
        homens += 1
    if idade > 18:
         idade2 += 1
    if sexo == 'F' and idade <20 :
        mulheres += 1
if cadastro == 'N':
    if sexo == 'M':
         homens += 1
    if idade > 18:
        idade2 += 1
    if sexo == 'F' and idade < 20:
        mulheres += 1
    break'''


tot18 = totH = totM20 = 0
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F]')).strip().upper()[0]
    if idade >= 18:
        tot18 += 1
    if sexo == 'M':
        totH += 1
    if sexo == 'F' and idade < 20:
        totM20 += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if resp == 'N':
        break
print (f'Total de pessoas com mais de 18 anos: {tot18}')
print (f'Ao todo temos {totH} homen(s) cadastrados.')
print (f'Temos {totM20} mulheres com menos de 20 anos.')
#correto
