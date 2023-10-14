# Exercício 67: Faça um programa que mostre a tabuadade vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.
numero = 1
while numero > 0:
    numero = int(input('Escreva um número inteiro positivo: '))
    if numero > 0:
        print('-'*50)
        print('A tabuada do número {} é:'.format(numero))
        for c in range (0,10):
            print('{} x {:2} = {}'.format(numero,c+1,numero*(c+1)))
    else:
        break
print('Número negativo. Programa finalizado!')
