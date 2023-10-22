# Exercício 99: Faça um programa que tenha uma função chamada maior() que receba vários parâmetros com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
from time import sleep
def lin():
    print('-='*30)
def maior(*int):
    print('Analisando os valores passados...')
    sleep(0.5)
    if len(int) == 0:
        print('Não foi inserido nenhum valor.')
    else:
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

maior(2,9,4,5,7,1)
maior(4,7,0)
maior(1,2)
maior(6)
maior()