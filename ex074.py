# 74: Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.
from time import sleep
print('Olá, vamos sortear 5 números entre 0 e 10...')
sleep(1)
from random import randint
"""aleatório_1 = randint(0,10)
aleatório_2 = randint(0,10)
aleatório_3 = randint(0,10)
aleatório_4 = randint(0,10)
aleatório_5 = randint(0,10)
tupla = (aleatório_1,aleatório_2,aleatório_3,aleatório_4,aleatório_5)"""
tupla = (randint(0,10),randint(0,10),randint(0,10),randint(0,10),randint(0,10)) # nessa opção não precisamos gravar variáveis
print(f'Os valores sorteados foram: {tupla}')
print(f'O menor valor gerado foi: {sorted(tupla)[0]}')
print(f'O maior valor gerado foi: {sorted(tupla)[-1]}')
