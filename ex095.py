# Exercício 95: Aprimore o desafio 93 par que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.
desempenho = []
jogador = {} # criei um novo dicionário nesse exercício
gols = []
soma_gols = 0
while True:
    jogador['nome']=input('Nome do jogador: ').capitalize()
    partidas=int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    gols.clear() # para limpar a lista gols a cada nova rodada
    for c in range (0,partidas):
        gols.append(int(input(f'Quantos gols na partida {c+1}? ')))
    jogador['gols'] = gols[:]
    jogador['total'] = sum(gols)
    desempenho.append(jogador.copy())
    while True:
        continua = input('Deseja continuar? [S/N] ').lower().strip()[0]
        if continua in 'sn':
            break
    if continua == 'n':
        break
    print('-'*50)
print('-='*25)
"""print(f'{"cod":<3} {"nome":<15}{"gols":<15}{"total":<6}')"""
print('cod ',end='')
for k in jogador.keys():
    print(f'{k:<15}',end='')
print()
for indice,dicionario in enumerate(desempenho):
    print(f'{indice:^4}',end='')
    for valor in dicionario.values(): # [imprime cada valor {dentro do dicionário} que está na lista]
        print(f'{str(valor):<15}',end='') #1 dicion compl a cada linha - imp todos da lista
    print()
# para o loop acima, precisamos inserir str(valor) para não dar erro
print('-'*50)
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar)'))
    if busca == 999:
        break
    if busca >= len(desempenho):
        print(f'ERRO! Não existe jogador com código {busca}!')
    else:
        print(f'  -- Levantamento do jogador {desempenho[busca]["nome"]}:')
        for i, g in enumerate(desempenho[busca]['gols']):
            print(f'No jogo {i+1} fez {g} gols.')
    print('-'*40)
print("<<VOLTE SEMPRE>>")
