# 53: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
frase = str(input('Digite uma frase qualquer: ')).lower().replace(" ","")
frase_invertida = frase[::-1]
print('De trás pra frente fica assim: {}'.format(frase_invertida))
if frase == frase_invertida:
    print('E por isso, esta frase é um PALÍNDROMO!!!')
else:
    print('E por isot, essa frase NÃO É UM PALÍNDROMO.')
