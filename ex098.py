"""Exercício 98: Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo e realize a contagem.
Seu programa tem que realizar três contagens através da função criada:
a) De 1 até 10, de 1 em 1
b) De 10 até 0, de 2 em 2
c) Uma contagem personalizada"""
from time import sleep
def lin():
    print('-='*20)
def contador(i,f,p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print(f'De {i} a {f}, de {p} em {p}:')
    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ',end='')
            sleep(0.5)
            cont += p
        print('FIM!')
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ',end='')
            sleep(0.5)
            cont -= p
        print('FIM!')
    lin()

contador(1,10,1)
contador(10,0,-2)
print('Agora é a sua vez de personalizar a contagem!')
inic = int(input('Início: '))
fim = int(input('Fim:    '))
pas = int(input('Passo:  '))
contador(inic,fim,pas)

