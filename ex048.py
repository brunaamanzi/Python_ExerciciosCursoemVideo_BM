# 48: Faça um programa que calcule a soma  o intervalo de 1 até 500.
"""import math
lista_numero = []
for numero in range (0,501,3):
    if numero % 2 != 0:
        lista_numero.append(numero)
from time import sleep
sleep(0.5)
print('Lista dos números ímpares múltiplos de 3 (de 0 a 500):')
sleep(0.5)
print(lista_numero)
sleep(0.5)
print('Soma entre todos os números: ')
sleep(0.5)
print(math.fsum(lista_numero))"""
# Outra forma de chegar no mesmo resultado:
soma = 0
cont = 0
for numero in range (1,501,2):
    if numero % 3 == 0:
        cont = cont + 1 # Contador
        soma += numero  # Acumulador
print('A quantidade de números que atendem à regra é \033[1;4m{}\033[m e a soma deles é \033[1;4m{}\033[m.'.format(cont,soma))

