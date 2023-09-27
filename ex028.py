# escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.
import time
print('-=-'*20)
print('Vou pensar em um número de 0 a 5... tente adivinhar!')
print('-=-'*20)
time.sleep(1)
import random
computador = random.randint(0,5)
jogador = int(input('Tente descobrir qual foi o número escolhido entre 0 e 5: '))
time.sleep(1)
print('Processando...')
time.sleep(1)
if computador == jogador :
    print('Você acertou! O número escolhido foi: {}!' .format(computador))
else:
    print('Você errou. O número escolhido foi {}.' .format(computador))
