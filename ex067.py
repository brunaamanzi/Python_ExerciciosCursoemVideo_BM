# Exercício 67: Faça um programa que mostre a tabuadade vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.
from time import sleep
numero = 1
while numero > 0:
    print('-' * 40)
    numero = int(input('\033[1;34mEscreva um número inteiro positivo: \033[m'))
    print('-' * 40)
    sleep(1)
    if numero > 0:
        print('A tabuada do número {} é:'.format(numero))
        for c in range (0,10):
            print('{} x {:2} = {}'.format(numero,c+1,numero*(c+1)))
    else:
        break
print('\033[1;31mNúmero negativo. Programa finalizado!\033[m')
