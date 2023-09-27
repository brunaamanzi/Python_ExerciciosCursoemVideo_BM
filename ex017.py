# Desafio 17: Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.
from math import sqrt, pow
cateto_oposto = float(input('Insira o comprimento do cateto oposto: '))
cateto_adjacente = float(input('Insira o comprimento do cateto adjacente: '))
hipotenusa = sqrt(cateto_adjacente**2+cateto_oposto**2)
#hipotenusa = math.hypot(cateto_oposto,cateto_adjacente)
print('A hipotenusa do triângulo Retângulo é {}'.format(hipotenusa))
#outra opção:
# co = float(input('informe o valor do cateto oposto: '))
# ca = float(input('informe o valor do cateto adjacente: '))
#hi = (co ** 2 + ca ** 2 )**(1/2)
#print('a hipotenusa vai medir {:.2f}'.format(hi))