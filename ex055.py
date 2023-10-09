# 55: Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.
lista_peso = []
for i in range (0,5):
    peso = float(input('{} Insira o seu peso em KG: '.format(i+1)))
    lista_peso.append(peso)
lista_peso.sort()
print('Olá! O menor peso lido foi {:.2f}kg e o maior peso lido foi {:.2f}kg.'.format(lista_peso[0],lista_peso[-1]))