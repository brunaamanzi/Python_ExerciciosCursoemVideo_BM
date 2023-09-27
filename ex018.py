#Desafio 18: Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
import math
angulo = float(input('Insira o ângulo: '))
#seno = math.sin(angulo*(3.14/180))
#cosseno = math.cos(angulo*(3.14/180))
#tangente = math.tan(angulo*(3.14/180))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
print('Seno {:.2f}\nCosseno {:.2f}\nTangente {:.2f}\nFIM'.format(seno,cosseno,tangente))
