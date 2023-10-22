# Exercício 103: Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.
def ficha(jogador,gol):
    if jogador == '':
        jogador='<desconhecido>'
    if gol == '':
        gol=0
    print(f'O jogador {jogador} fez {gol} gol(s) no campeonato.')


jog = input('Nome do jogador: ').capitalize()
g = input('Número de gols: ')
ficha(jog,g)