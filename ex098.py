"""Exercício 98: Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo e realize a contagem.
Seu programa tem que realizar três contagens através da função criada:
a) De 1 até 10, de 1 em 1
b) De 10 até 0, de 2 em 2
c) Uma contagem personalizada"""
from time import sleep()
def lin():
    print('-='*20)
lin()
def contador(i,f,p):
    print(f'De {i} a {f}, de {p} em {p}:')
    for c in range(i,f+1,p):
        print(c,end=' ')
        sleep(0.5)
    print('FIM!')
contador(1,10,1)
lin()
def contador(f,i,p):
    print(f'De {f} a {i}, de {p} em {p}:')
    for c in range(f,i,p):
        print(c,end=' ')
        sleep(0.5)
    print('FIM!')
contador(10,-1,-2)
lin()
def contador(f,i,p):
    print(f'De {f} a {i}, de {p} em {p}:')
    for c in range(f,i,p):
        print(c,end=' ')
        sleep(0.5)
    print('FIM!')
contador(50,-1,-2)

