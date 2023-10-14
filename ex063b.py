# 63: escreva um programa que leia um número "n" inteiro qualquer e mostre na tela os "n" primeiros elementos de uma sequência de FIBONACCI.
print('-*'*20)
print('{:^38}'.format('SEQUÊNCIA DE FIBONACCI'))
print('-*'*20)
n = int(input('Insira o número de elementos que você deseja ver: '))
t1 = 0
t2 = 1
cont = 3
print('{} -> {} -> '.format(t1,t2),end='')
while n >= cont:
    t3 = t1 + t2
    print('{} -> '.format(t3),end='')
    cont += 1
    t1 = t2
    t2 = t3
print('fim')