# """ 59: Crie um programa que leia dois valores e mostre um menu na tela:
# [1] SOMAR
# [2] MULTIPLICAR
# [3] MAIOR
# [4] NOVOS NÚMEROS
# [5] SAIR DO PROGRAMA
# Seu programa deverá realizar a operação solicitada em cada caso."""
n_1 = int(input('Escolha um número: '))
n_2 = int(input('Escolha outro número: '))
lista = []
opção = 0
from time import sleep
while opção != 5:
    print('''[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa''')
    opção = int(input('\033[1;31mEscolha a sua opção: \033[m'))
    if opção == 1:
        soma = n_1 + n_2
        print('O resultado de {} + {} é {}.'.format(n_1,n_2,soma))
    elif opção == 2:
        multiplicação = n_1 * n_2
        print('O resultado de {} * {} é {}.'.format(n_1,n_2,multiplicação))
    elif opção == 3:
        lista.append(n_1)
        lista.append(n_2)
        lista.sort()
        print('Entre {} e {}, o maior é {}.'.format(n_1,n_2,lista[-1]))
    elif opção == 4:
        n_1 = int(input('Escolha um número: '))
        n_2 = int(input('Escolha outro número: '))
    elif opção == 5:
        print('Finalizando...')
    sleep(1)
print('Jogo encerrado! Volte sempre.')






