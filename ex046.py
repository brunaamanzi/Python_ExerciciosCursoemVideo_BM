# 46: Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.
from time import sleep
contagem = [0,1,2,3,4,5,6,7,8,9,10]
contagem.sort(reverse=True)
for contagem in contagem:
    print(contagem)
    sleep(1)
print('Hora dos fogos!!! ´*´*´*´*´*')

