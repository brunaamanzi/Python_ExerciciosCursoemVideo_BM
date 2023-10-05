# 46: Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.
from time import sleep
"""contagem = [0,1,2,3,4,5,6,7,8,9,10]
for i in range (0,11):
    contagem.sort(reverse=True)
    print(contagem[i])
    sleep(1)
print('Hora dos fogos!!! ´*´*´*´*´*')"""
for i in range (10,-1,-1):
    print(i)
    sleep(0.5)
print('BUMMMM! POOOM! * * * * * * * * * *')
