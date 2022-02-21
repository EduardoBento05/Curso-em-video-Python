#Exercício Python 57: Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’. Caso esteja errado, peça a digitação novamente até ter um valor correto.
sexo = str(input('Digite o sexo da pessoa [M] para masculino e [F] para femenino: ')).upper()
while sexo not in 'MmFf':
    sexo = str(input('Digite novament o sexo da pessoa [M] para masculino e [F] para femenino: ')).upper()    
print('sexo {} registrado com sucesso!'.format(sexo))
#correto