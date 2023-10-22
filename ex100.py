# Exercício 100: Faça um programa que tenha uma lista chamada números e duas funções sorteia() e somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro da lista, e a segunda função vai mostrar a soma entre todos os valores PARES sorteados pela função anterior.
from random import randint
from time import sleep
números = [randint(0,10),randint(0,10),randint(0,10),randint(0,10),randint(0,10)]

def sorteia():
    print('Sorteando 5 valores da lista: ',end='')
    for c in números:
        print(c,end=' ')
        sleep(0.5)
    print('PRONTO!')

def somapar():
    par = 0
    print(f'Somando os valores pares de {números}, temos ',end='')
    for c in números:
        if c % 2== 0:
            par += c
    print(par)

sorteia()
somapar()