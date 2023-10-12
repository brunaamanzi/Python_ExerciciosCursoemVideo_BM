# 63: escreva um programa que leia um número "n" inteiro qualquer e mostre na tela os "n" primeiros elementos de uma sequência de FIBONACCI.
print('-*'*20)
print('{:^38}'.format('SEQUÊNCIA DE FIBONACCI'))
print('-*'*20)
n = int(input('Insira o número de elementos que você deseja ver: '))
sequencia_fibonacci = [0,1]
while len(sequencia_fibonacci) < n:
    sequencia_fibonacci.append(sequencia_fibonacci[-1]+sequencia_fibonacci[-2])
print(sequencia_fibonacci)