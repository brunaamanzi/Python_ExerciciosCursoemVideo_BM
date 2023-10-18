'''Exercício 75: Desenvolva um programa que leia 4 valores no teclado e coloque numa tupla. No final, mostre:
a) quantas vezes apareceu o valor 9;
b) em que posição foi digitado o primeiro valor 3;
c) quais foram os números pares'''
print('-'*30)
print('Olá! Pense em 4 números...')
print('-'*30)
from time import sleep
sleep(1)
"""n1 = int(input('Insira um número: '))
n2 = int(input('Insira outro número: '))
n3 = int(input('Insira mais um número: '))
n4 = int(input('Insira o último número: '))
par1 = par2 = par3 = par4 = 0
tupla = (n1,n2,n3,n4)"""
tupla = (int(input('Insira um número: ')),int(input('Insira outro número: ')),int(input('Insira mais um número: ')),int(input('Insira o último número: ')))
print(f'Os valores digitados foram: {tupla}')
if 9 in tupla:
    print(f'O valor 9 apareceu {tupla.count(9)} vezes.')
else:
    print('O valor 9 não apareceu nenhuma vez.')
if 3 in tupla:
    print(f'O valor 3 apareceu na {tupla.index(3)+1}ª posição.')
else:
    print('O valor 3 não apareceu em nenhuma posição.')
print('Os números pares que apareceram foram:',end=' ')
for c in tupla:
    if c % 2 == 0:
        print(c,end=' ')
"""if tupla[0] % 2 == 0:
    par1 = tupla[0]
if tupla [1] % 2 == 0:
    par2 = tupla[1]
if tupla [2] % 2 == 0:
    par3 = tupla[2]
if tupla[3] % 2 == 0:
    par4 = tupla[3]
pares = (par1,par2,par3,par4)
print(f'Os números pares que apareceram foram: {pares}')"""




