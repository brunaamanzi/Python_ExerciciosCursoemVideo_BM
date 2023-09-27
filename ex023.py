# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
#ex: digite um número: 3420
# unidade: 0
# dezena: 2
# centena: 4
# milhar: 3

numero = int(input('digite um número: '))
#print('unidade: {}'.format(numero[-1]))
#print('dezena: {}'.format(numero[-2]))
#print('centena: {}'.format(numero[-3]))
#print('milhar: {}'.format(numero[-4]))
unid = numero // 1 % 10
dez = numero // 10 % 10
cen = numero // 100 % 10
mil = numero // 1000 % 10
print("unidade: {}\ndezena: {}\ncentena: {}\nmilhar: {}".format(unid,dez,cen,mil))

# num = int(input('Digite um numero: '))
# n = num + 10000
# nn = str(n)
# print(f'A unidade é: {nn[-1]}')
# print(f'A dezena é: {nn[-2]}')
# print(f'A centena é: {nn[-3]}')
# print(f'O milhar é: {nn[1]}')

