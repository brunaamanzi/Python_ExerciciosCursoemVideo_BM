# Exercício 99: Faça um programa que tenha uma função chamada maior() que receba vários parâmetros com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
from time import sleep
def lin():
    print('-='*30)
def maior(*int):
    print('Analisando os valores passados...')
    sleep(0.5)
    for valor in int:
        print(valor,end=' ')
    print()
    sleep(0.5)
    print(f'Foram informados {len(int)} valores ao todo...')
    sleep(0.5)
    m = sorted(int)[-1]
    print(f'O maior número inserido foi {m}')
    sleep(0.5)
    lin()

maior(3,6,5,1,3,9,6,4,18,0)
maior(7,5,3)
maior(0)
maior(6,3,8,6)