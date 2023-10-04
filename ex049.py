# 49: refaça o desafio 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.
#Desafio 09: Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada.

numero = int(input('Escreva um número inteiro qualquer: '))
print('-'*50)
print('A tabuada do número {} é:'.format(numero))
for _ in range (0,10):
    tabuada = numero * (_+1)
    print(numero,' x ',_+1,'=',tabuada)


