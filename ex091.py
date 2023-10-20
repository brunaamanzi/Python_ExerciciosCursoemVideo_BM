# Exercício 91: Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
from time import sleep
from random import randint
from operator import itemgetter
jogo = {}
ranking = {}
# Também poderia colocar tudo direto dentro do dicionário:
"""jogo={'jogador1': randint(0,6),
            'jogador2': randint(0,6),
            'jogador3': randint(0,6),
            'jogador4': randint(0,6)}"""
jogo['jogador1'] = randint(0,6)
jogo['jogador2'] = randint(0,6)
jogo['jogador3'] = randint(0,6)
jogo['jogador4'] = randint(0,6)
print('-'*30)
print(f'{"Valores sorteados:":^30} ')
print('-'*30)
sleep(0.5)
for k,v in jogo.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)
print('-'*30)
print(f'{"RANKING DOS JOGADORES":^30}')
print('-'*30)
sleep(0.5)
ranking = sorted(jogo.items(),key=itemgetter(1),reverse=True) # ao utilizar a função sorted, ela transforma em lista
for i, v in enumerate(ranking):
    print(f'{i+1}º Lugar: {v[0]} com {v[1]} pontos.')
    sleep(1)





