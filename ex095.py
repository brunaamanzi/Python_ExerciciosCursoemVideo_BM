# Exercício 95: Aprimore o desafio 93 par que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.
desempenho = []
jogador = {}
gols = []
soma_gols = 0
while True:
    jogador['nome']=input('Nome do jogador: ').capitalize()
    partidas=int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    for c in range (0,partidas):
        gol = int(input(f'Quantos gols na partida {c}? '))
        gols.append(gol)
        soma_gols += gol
    jogador['gols'] = gols
    jogador['total'] = soma_gols
    desempenho.append(jogador.copy())
    while True:
        continua = input('Deseja continuar? [S/N] ').lower().strip()[0]
        if continua in 'sn':
            break
    if continua == 'n':
        break
    print('-'*50)
print('-='*25)
print(f'{"cod":<3} {"nome":<15} {"gols":<15} {"total":<6}')
for i,c in enumerate(desempenho):
    print(f'{i:<3} {c["nome"]:<15} {c["gols"]:<15} {c["total"]:<6}')
print('-'*50)

