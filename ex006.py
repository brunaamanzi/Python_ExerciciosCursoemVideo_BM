#Desafio 06: Crie um algorítmo que leia um número e mostre o seu dobro, triplo e raíz quadrada.
n1 = int(input('Escreva um número: '))
print('O número é {}, seu dobro é {}, seu triplo é {} e sua raíz quadrada é {:.2f}.'.format(n1,n1*2,n1*3,n1**(1/2)))
#outra forma de calcular a raíz quadrada: pow(n1,(1/2)