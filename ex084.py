"""Exercício 84: Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
a) quantas pessoas foram cadastradas;
b) uma listagem com as pessoas mais pesadas;
c) uma listagem com as pessoas mais leves."""
lista = []
dados = []
continua = ''
while True:
    lista.append(str(input('Insira o nome: ')))
    lista.append(int(input('Insira o peso: ')))
    dados.append(lista[:])
    lista.clear()
    while True:
        continua = input('Deseja continuar? [S/N] ').lower().strip()[0]
        if continua in 'sn':
            break
    if continua == 'n':
        break
print('-'*40)
print(f'O \033[1;34mnúmero de pessoas cadastradas\033[m foi {len(dados)}.')
print('-'*40)
from operator import itemgetter
dados.sort(key=itemgetter(1),reverse=True)
print('\033[1;34mSegue a relação ordenada pelas pessoas mais pesadas: \033[m')
print(f'{"Nome":<17}', end='')
print(f'{"Peso KG":>12}')
for p in dados:
    print(f'{p[0]:.<17}',end='')
    print(f'{p[1]:.>8} KG')
dados.sort(key=itemgetter(1),reverse=False)
print('-' * 40)
print('\n\033[1;34mSegue a relação ordenada pelas pessoas mais leves: \033[m')
print(f'{"Nome":<15}', end='')
print(f'{"Peso KG":>12}')
for p in dados:
    print(f'{p[0]:.<15}',end='')
    print(f'{p[1]:.>8} KG')
print('-'*40)
print('fim')