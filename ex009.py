#Desafio 09: Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada.
numero = int(input('Escreva um número inteiro qualquer: '))
#print('Tabuada do número {}:\n{}* 1= {}\n{}* 2= {}\n{}* 3= {}\n{}* 4= {}\n{}* 5= {}\n{}* 6= {}\n{}* 7= {}\n{}* 8= {}\n{}* 9= {}\n{}*10= {}'.format(numero,numero,numero*1,numero,numero*2,numero,numero*3,numero,numero*4,numero,numero*5,numero,numero*6,numero,numero*7,numero,numero*8,numero,numero*9,numero,numero*10))
print('-'*30)
print('{} x {:2} = {}'.format(numero,1,numero*1))
print('{} x {:2} = {}'.format(numero,2,numero*2))
print('{} x {:2} = {}'.format(numero,3,numero*3))
print('{} x {:2} = {}'.format(numero,4,numero*4))
print('{} x {:2} = {}'.format(numero,5,numero*5))
print('{} x {:2} = {}'.format(numero,6,numero*6))
print('{} x {:2} = {}'.format(numero,7,numero*7))
print('{} x {:2} = {}'.format(numero,8,numero*8))
print('{} x {:2} = {}'.format(numero,9,numero*9))
print('{} = {:2} = {}'.format(numero,10,numero*10,))
print('-fim-'*15)


