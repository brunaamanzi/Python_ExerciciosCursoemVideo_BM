# Desafio 16: Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira.

import math
num = float(input('Digite um valor: '))
#int = trunc(float)
#print('O número {} tem a parte inteira {}.'.format(float,int))
print('O valor digitado foi {} e sua porção inteira é {}.'.format(num,math.trunc(num)))
#outra opção com int
#print('O valor digitado foi {} e sua porção inteira é {}'.format(num,int(num)))