# Exercício 78: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
lista = []
print('Olá! Por gentileza, escolha 5 números:')
for c in range (0,5):
    lista.append(int(input(f'Insira um número na posição {c}: ')))
print(f'Você digitou os valores \033[1;32m{lista}\033[m')
print(f'O maior valor digitado foi \033[1;32m{max(lista)}\033[m e sua posição na lista é: ', end='')
for i, c in enumerate(lista):
    if c == max(lista):
        print(f'{i}, ',end='')
print(f'\nO menor valor digitado foi \033[1;32m{min(lista)}\033[m e sua posição na lista é: ', end='')
for i, c in enumerate(lista):
    if c == min(lista):
        print(f'{i}, ',end='')
