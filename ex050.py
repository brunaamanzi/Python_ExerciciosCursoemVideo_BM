# 50: desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.
soma = 0
cont = 0
for c in range (1,7):
    num = int(input('Escreva um número: '))
    if num != 0 and num % 2 == 0:
        soma += num
        cont += 1
"""print('Números pares: {}\nSoma dos números pares: {}'.format(numeros_pares,fsum(numeros_pares)))"""
print('A quantidade de números pares é {} e a soma é {}.'.format(cont,soma))

