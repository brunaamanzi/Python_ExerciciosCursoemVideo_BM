"""Exercício 84: Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
a) quantas pessoas foram cadastradas;
b) uma listagem com as pessoas mais pesadas (maior peso e nome da pessoa);
c) uma listagem com as pessoas mais leves (menor peso e nome da pessoa)."""
lista = []
dados = []
continua = ''
maior = menor = 0
while True:
    lista.append(str(input('Insira o nome: ')).capitalize())
    lista.append(float(input('Insira o peso: ')))
    if len(dados) == 0:
        maior = menor = lista[1]
    else:
        if lista[1] > maior:
            maior = lista[1]
        if lista[1] < menor:
            menor = lista
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
print(f'O \033[1;34mmaior peso\033[m cadastrado foi {maior}, de: ',end='')
for p in dados:
    if maior in p:
        print(f'[{p[0]}]',end=' ')
print()
print('-'*40)
print(f'O \033[1;34mmenor peso\033[m cadastrado foi {menor}, de: ',end='')
for p in dados:
    if menor in p:
        print(f'[{p[0]}]',end=' ')
print()
print('-'*40)


# O problema no código abaixo é que se duas pessoas tiverem o menor ou o maior peso, o código só traz a primeira ocorrência.
"""from operator import itemgetter
dados.sort(key=itemgetter(1),reverse=True)
print(f'O \033[1;34mmaior peso\033[m foi {dados[0][1]}, de {dados[0][0]}.')
print('-' * 40)
print(f'O \033[1;34mmenor peso\033[m foi {dados[-1][1]}, de {dados[-1][0]}.')"""
