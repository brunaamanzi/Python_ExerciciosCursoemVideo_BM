# 58: Melhore o jogo do desafio 28 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora, o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

import time
print('-=-'*20)
print('\033[40mVou pensar em um número de 0 a 10... tente adivinhar!\033[m')
print('-=-'*20)
time.sleep(1)
from random import randint
jogador = 0
palpites = 1
computador = randint(0,10)
while jogador == 0:
    j = int(input('Tente descobrir qual foi o número escolhido entre 0 e 10: '))
    if j == computador:
        jogador += 1
        print('\033[43mVocê ganhou!\033[m')
    else:
        if computador > j:
            print('\033[41mGanhei! Sou maior... Tente novamente\033[m')
        elif computador < j:
            print('\033[41mGanhei! Sou menor... Tente novamente\033[m')
        palpites += 1
print('O número de tentativas foi {}'.format(palpites))
