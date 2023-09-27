#Desafio 08: Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
valor = float(input('Valor em metros: '))
print('O valor em metros é {:.0f}m, em centímetros é {:.0f}cm e em milímetros é {}mm.'.format(valor,valor*100,valor*1000))
print('ou')
print('{}cm \n {}mm'.format(valor*100,valor*1000))