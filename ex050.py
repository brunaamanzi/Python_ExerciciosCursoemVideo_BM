# 50: desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.
from math import fsum
numeros_pares = []
for c in range (0,6):
    numero = int(input('Escreva um número: '))
    if numero % 2 == 0:
        numeros_pares.append(numero)
print('Números pares: {}\nSoma dos números pares: {}'.format(numeros_pares,fsum(numeros_pares)))

