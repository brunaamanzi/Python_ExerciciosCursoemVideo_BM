# Exercício 88: Faça um programa que ajude um jogador da MEGA SENA a criar palpites. O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
print('-'*40)
print(f'{"BEM VINDO AO PALPITE MEGA SENA!":^40}')
print('-'*40)
from time import sleep
from random import randint
sleep(1)
print('Vamos iniciar...')
sleep(1)
jogos = int(input('Quantos jogos serão gerados? '))
sleep(1)
palpite = []
palpites = []
aleatório = 0
for c in range (0,jogos):
    aleatório = randint(0,60),randint(0,60),randint(0,60),randint(0,60),randint(0,60),randint(0,60)
    palpite.append(aleatório)
    palpites.append(palpite[:])
    palpite.clear()
print(f'Você jogará {jogos} vezes. Aqui está nossa sugestão:')
for p in palpites:
    print(p)