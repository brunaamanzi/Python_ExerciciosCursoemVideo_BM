#Desafio 11: Faça um programa que leia a largura e a altura de uma parede em metros. Calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m².
largura=float(input('Informe a largura da parede em metros: '))
altura=float(input('Informe a altura da parede em metros: '))
area=largura*altura
print('Area: {}m²\nQuantidade de tinta necessária: {} litros'.format(area,area/2))

