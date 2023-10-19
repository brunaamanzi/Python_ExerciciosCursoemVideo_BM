# Exercício 86: Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado. No final, mostre a matriz na tela, com a formatação correta.
matriz = [[],[],[]]
for c in range (0,3):
    matriz[0].append(int(input(f'Insira um valor para [0, {c}]: ')))
for c in range (0,3):
    matriz[1].append(int(input(f'Insira um valor para [1, {c}]: ')))
for c in range (0,3):
    matriz[2].append(int(input(f'Insira um valor para [2, {c}]: ')))
print('-'*30)
for c in matriz[0]:
    print(f'[ {c} ]',end='')
print()
for c in matriz [1]:
    print(f'[ {c} ]',end='')
print()
for c in matriz [2]:
    print(f'[ {c} ]',end='')
print()
print('-'*30)
print(matriz)
"""print(matriz[0])
print(matriz[1])
print(matriz[2])"""
