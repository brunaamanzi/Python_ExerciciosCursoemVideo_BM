# Exercício 103: Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.
def ficha(jogador='<desconhecido>',gol=0):
    print(f'O jogador {jogador} fez {gol} gol(s) no campeonato.')


jog = input('Nome do jogador: ').capitalize().strip()
g = input('Número de gols: ').strip()
if g.isnumeric():
    g = int(g) # para transformar a variável em inteiro
else:
    g = 0 # se for texto, retornará o valor 0
if jog == '':
    ficha(gol=g)
else:
    ficha(jog,g) # se os dois valores forem preenchidos
