# 49: refaça o desafio 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.
#Desafio 09: Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada.
numero = int(input('Escreva um número inteiro qualquer: '))
print('-'*50)
print('A tabuada do número {} é:'.format(numero))
for c in range (0,10):
    """print(numero,' x ',c+1,'=',tabuada)"""
    print('{} x {:2} = {}'.format(numero,c+1,numero*(c+1)))


