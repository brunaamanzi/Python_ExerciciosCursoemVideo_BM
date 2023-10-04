# 53: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
from time import sleep
frase = str(input('Digite uma frase qualquer: '))
sleep(1)
print('Vamos verificar se ela é um palíndromo...')
sleep(1)
if frase.reversed(True) == frase:
    print('Palíndromo')