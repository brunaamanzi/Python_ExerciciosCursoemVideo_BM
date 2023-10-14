""" 60: Faça um programa que leia um número qualquer e mostre o seu fatorial.
exemplo: 5! = 5x4x3x2x1 = 120"""
n = int(input('Insira um número inteiro: '))
c = n
f = 1
print('Calculando {}! = '.format(n),end='')
while c > 0:  # ou: for c in range (1,n+1):
    print('{}'.format(c),end='')
    print(' x ' if c > 1 else ' = ',end='')
    f *= c
    c -= 1
print(f)



