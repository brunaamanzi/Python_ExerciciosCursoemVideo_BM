# Exercício 95: Aprimore o desafio 93 par que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.
desempenho = {}
gols = []
soma_gols = 0
while True:
    desempenho['nome']=input('Nome do jogador: ').capitalize()
    partidas=int(input(f'Quantas partidas {desempenho["nome"]} jogou? '))
    for c in range (0,partidas):
        gol = int(input(f'Quantos gols na partida {c}? '))
        gols.append(gol)
        soma_gols += gol
    while True:
        continua = input('Deseja continuar? [S/N] ').lower().strip()[0]
        if continua in 'sn':
            break
    if continua == 'n':
        break
    print('-'*40)
print('-='*20)
desempenho['gols']=gols
desempenho['total']=soma_gols
print(f'{"cod":<3} {"nome":<15} {"gols":<15} {"total":<6}')
for c in range (0,len(desempenho)):
    print(f'{c:<3}') {desempenho["nome"]:<15} {gols:<15} {desempenho["total"]:<6}')
print('-'*40)


