# Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para Fahrenheit.
celsius = float(input('Informe a temperatura em ºC: '))
fahrenheit = (celsius*1.8)+32
print('A temperatura é \n{} ºC\n{} ºF'.format(celsius,fahrenheit))
