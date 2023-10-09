# 52: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
num = int(input('Insira um número: '))
primo = 0
for c in range (1,num + 1):
    if num % c == 0:
        print('\033[32m',end='')
        primo += 1
    else:
        print('\033[31m',end='')
    print('{} '.format(c), end='')
print('\033[m\nO número {} é divisível por {} números.'.format(num,primo))
if primo > 2:
    print('E por isso ele NÃO É PRIMO!!!')
else:
    print('E por isso ele É PRIMO!!!')