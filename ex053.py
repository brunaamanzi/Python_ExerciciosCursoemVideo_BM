# 53: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
from time import sleep
lista = []
frase = str(input('Digite uma frase qualquer: ')).replace(" ","")
lista.append(frase)
lista_invertida = frase[::-1]
if frase == lista_invertida:
    print('Esta frase é um PALÍNDROMO!!!')
else:
    print('Essa frase não é um Palíndromo.')
