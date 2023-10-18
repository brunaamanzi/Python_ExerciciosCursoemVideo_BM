# Exercício 78: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
lista = []
print('Olá! Por gentileza, escolha 5 números:')
for c in range (0,5):
    lista.append(int(input(f'Insira um número na posição {c}: ')))
for i, c in enumerate(lista):
    if c == max(lista):
        print(f'O maior valor digitado foi {c} e sua posição na lista é {i}.')
    if c == min(lista):
        print(f'O menor valor digitado foi {c} e sua posição na lista é {i}.')
