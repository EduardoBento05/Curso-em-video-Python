d = input('Digite alguma coisa :')
print('O tipo Primitivo deste valor é :', type(d))
print('É um numero?', d.isnumeric())
print('Só tem espaço?', d.isspace())
print('É Alfabético?', d.isalpha())
print('É um Alfanumérico?', d.isalnum())
print('Está em Maiuscula?', d.isupper())
print('Está em Minuscula?',d.islower())
print('Está capitalizado?', d.istitle())