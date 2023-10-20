# Exercício 91: Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
from random import randint
from operator import itemgetter
resultados = {}
resultados['jogador1'] = randint(0,6)
resultados['jogador2'] = randint(0,6)
resultados['jogador3'] = randint(0,6)
resultados['jogador4'] = randint(0,6)
print('-'*30)
print(f'{"Valores sorteados:":^30} ')
print('-'*30)
for k,v in resultados(items):
    print(f'{k} tirou {v} no dado.')
print('*'*30)
print(f'{"RANKING DOS JOGADORES":^30}')
print('-'*30)



