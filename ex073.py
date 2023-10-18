"""73: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois, mostre:
a) apenas os 5 primeiros colocados;
b) os últimos 4 colocados da tabela;
c) uma lista com os times em ordem alfabética;
d) em que posição na tabela está o time da Chapecoense."""
print('-'*50)
print(f'\033[1;34m{"Tabela do Campeonato Brasileiro de Futebol":^49}\033[m')
print('-'*50)
times = ('Flamengo','Santos','Palmeiras','Gremio','Atletico Paranaense','São Paulo','Internacional','Conrithians','Fortaleza','Goias','Bahia','Vasco','Atletico Mineiro','Fluminense','Botafogo','Ceará','Cruzeiro','CSA','Chapecoense','Avaí')
print(f'\033[1;34mOs 20 primeiros colocados:\033[m\n{times}')
print(f'\033[1;34mOs 5 primeiros colocados:\033[m\n{times[0:5]}')
print(f'\033[1;34mOs 4 últimos colocados:\033[m\n{times[-4:]}')
print(f'\033[1;34mRelação dos times em Ordem Alfabética:\033[m\n{sorted(times)}')
print(f'\033[1;34mO Chapecoense está na {times.index("Chapecoense")+1}ª posição.\033[m')


