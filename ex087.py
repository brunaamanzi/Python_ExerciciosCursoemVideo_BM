"""Exercício 87: Apromore o desafio anterior, mostrando no final:
a) a soma de todos os valores pares digitados;
b) a soma dos valores da terceira coluna;
c) o maior valor da segunda linha."""
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
par = 0
for sublista in matriz:
    for item in sublista:
        if item % 2 == 0:
            par += item
print(f'A soma dos valores pares é: {par}')
soma = matriz[0][2] + matriz[1][2] + matriz[2][2]
print(f'A soma dos valores da terceira coluna é: {soma}')
matriz[1].sort()
print(f'O maior valor da segunda linha é {matriz[1][2]}')

