# Exercício 93: Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonado.
desempenho = {}
gols = []
soma_gols = 0
desempenho['nome']=input('Nome do jogador: ')
partidas=int(input(f'Quantas partidas {desempenho["nome"]} jogou? '))
for c in range (0,partidas):
    gol = int(input(f'Quantos gols na partida {c}? '))
    gols.append(gol)
    soma_gols += gol
desempenho['gols']=gols[:] # ou: desempenho['gols']=sum(gols)
desempenho['total']=soma_gols
print('-'*40)
print(desempenho)
print('-'*40)
for k,v in desempenho.items():
    print(f'O campo {k} tem o valor {v}.')
print('-'*40)
print(f'O jogador {desempenho["nome"]} jogou {partidas} partidas.')
for i,g in enumerate(gols):
    print(f'    => Na partida {i}, fez {g} gols.')
print(f'Foi um total de {soma_gols} gols.')

