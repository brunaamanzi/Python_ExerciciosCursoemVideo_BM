#faça um programa que leia três números e mostre qual é o maior e qual é o menor.
import time
n1 = int(input('Insira um número: '))
n2 = int(input('Insira outro número: '))
n3 = int(input('Insira mais um número: '))
time.sleep(1)
print('PROCESSANDO...')
time.sleep(1)
lista = [n1,n2,n3]
lista.sort()
print('O maior número é {}.'.format(lista[-1]))
print('O menor número é {}.'.format(lista[0]))

#print('O maior número é {}.'.format(n[]))

