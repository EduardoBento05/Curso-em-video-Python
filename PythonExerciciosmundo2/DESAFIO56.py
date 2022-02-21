#Exercício Python 56: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos
soma = 0
nomemaioridade = ''
idademaiorsexom = 0
idademenorsexom = 0
idademenorsexof = 0
for c in range (1,5):
    nome = str(input('Digite o {}º nome: '.format(c))).upper().strip()
    sexo = str(input("Digite (F)Feminino e (M)Masculino para a {}ª pessoa: ".format(c))).upper().strip()
    idade = float(input('Digite a {}ª idade: '.format(c)))
    soma = soma + idade
    media = soma/4
    if sexo == 'M':
        if c == 1: # vai calcular a idade do homem de maior e idade e menor idade e coloca o nome do homem mais velho
            idademaiorsexom = idade
            nomemaioridade = nome
            idademenorsexom = idade
        else:
            if idade > idademaiorsexom:
                idade = idademaiorsexom
                nomemaioridade = nome
            if idade < idademenorsexom:
                 idademenorsexom = idade
    else:
        if idade < 20: #mostra quantas mulheres são menores de 20 anos
            idademenorsexof += 1
print('A Média das idades é igual a {:.2f}'.format(media))
print('A idade do homem mais velho é {:.1f} e o seu nome é {}'.format(idademaiorsexom,nomemaioridade))
print('Existem {} mulher(es) que tem a idade menor de 20 anos'.format(idademenorsexof))
#correto



