"""Exercício 87: Apromore o desafio anterior, mostrando no final:
a) a soma de todos os valores pares digitados;
b) a soma dos valores da terceira coluna;
c) o maior valor da segunda linha."""
matriz = [[],[],[]]
soma_pares = terceira_coluna = segunda_linha = 0
for l in range (0,3):
    for c in range (0,3):
        matriz[l].append(int(input(f'Digite um valor para [{l}, {c}]: ')))
print('-'*30)
for l in range (0,3):
    for c in range (0,3):
        print(f'[{matriz[l][c]:^5}]',end='')
        if matriz[l][c] % 2 == 0:
            soma_pares += matriz[l][c]
    print()
print('-'*30)
"""for lista in matriz:
    for sublista in lista:
        if sublista % 2 == 0:
            soma_pares += sublista"""
print(f'A soma dos números pares inseridos é: {soma_pares}.')
# terceira_coluna = matriz[0][2] + matriz[1][2] + matriz[2][2]
for l in range (0,3):
    terceira_coluna += matriz[l][2]
print(f'A soma dos números inseridos na terceira coluna é: {terceira_coluna}')
segunda_linha = sorted(matriz[1])
print(f'O maior número inserido na segunda linha é: {segunda_linha[-1]}')
print('-'*30)