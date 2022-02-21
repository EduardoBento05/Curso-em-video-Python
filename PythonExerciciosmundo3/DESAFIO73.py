'''Exercício Python 73: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética.
d) Em que posição está o time da Chapecoense'''

brasileirão = ('ATLETICO MINEIRO','FLAMENGO','SÃO PAULO','INTERNACIONAL','PALMEIRAS','FLUMINENSE','SANTOS','SPORT RECIFE','FORTALEZA','VASCO DA GAMA','GREMIO','BAHIA','CORINTHIANS','ATLETICO GOIENIENSE','BOTAFOGO','ATHLETICO-PR','CEARÁ','CORITIBA','BRAGANTINO','CHAPECOENSE') 
print(f'Os 5 primeiro colocados são {brasileirão[0:5]}')#mostras os 5 primeiros times
print(f'Os 5 últimos 4 colocados são{brasileirão[-4:]}')#mostra os 4 ultimos colocados
print(f'{sorted(brasileirão)}')#deixa a tupla em ordem alfabética através do comando sorted
print('O time da Chapecoense está na {} posição '.format(brasileirão.index('CHAPECOENSE')+1))#busca a posição através do comando .index e o +1 pois a tupla começa contando do espaço 0.obs: a chapecoense estã na segunda divisão usei só para fazer o exercício.
#correto