# 53: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
from time import sleep
frase = str(input('Digite uma frase qualquer: ')).lower().replace(" ","")
lista_invertida = frase[::-1]
print('De trás pra frente fica assim: {}'.format(lista_invertida))
if frase == lista_invertida:
    print('E por isso, esta frase é um PALÍNDROMO!!!')
else:
    print('E por isot, essa frase NÃO É UM PALÍNDROMO.')
