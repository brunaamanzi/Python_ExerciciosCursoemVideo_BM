"""Exercício 84: Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
a) quantas pessoas foram cadastradas;
b) uma listagem com as pessoas mais pesadas (maior peso e nome da pessoa);
c) uma listagem com as pessoas mais leves (menor peso e nome da pessoa)."""
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
print(f'O \033[1;34mmaior peso\033[m foi {dados[0][1]}, de {dados[0][0]}.')
print('-' * 40)
print(f'O \033[1;34mmenor peso\033[m foi {dados[-1][1]}, de {dados[-1][0]}.')
print('-'*40)
print('fim')