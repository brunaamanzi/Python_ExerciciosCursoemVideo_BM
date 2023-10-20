# Exercício 88: Faça um programa que ajude um jogador da MEGA SENA a criar palpites. O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
from random import sample
print('-'*40)
print(f'{"BEM VINDO AO PALPITE MEGA SENA!":^40}')
print('-'*40)
from time import sleep
sleep(1)
print('Vamos iniciar...')
sleep(1)
jogos = int(input('Quantos jogos serão gerados? '))
sleep(1)
palpites = []
aleatório = 0
for c in range (0,jogos):
    palpite = sample(range(0,60),6) # Gera 6 números únicos entre 1 e 60 já numa lista
    palpite.sort()
    palpites.append(palpite[:])
print(f'Você jogará {jogos} vezes. Aqui está nossa sugestão:')
for i, p in enumerate(palpites):
    print(f'{i+1}º palpite: {p}')
    sleep(0.5)
