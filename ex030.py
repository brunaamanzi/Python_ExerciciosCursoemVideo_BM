#crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.
import math
numero = int(input('Escreva um número inteiro: '))
if numero % 2 == 0 :
    print('O número é par.')
else:
    print('O número é ímpar.')