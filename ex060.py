""" 60: Faça um programa que leia um número qualquer e mostre o seu fatorial.
exemplo: 5! = 5x4x3x2x1 = 120"""
num = int(input('Insira um número inteiro: '))
resultado = 1
lista_fatorial = []
while num > 0:
    lista_fatorial.append(num)
    resultado *= num
    num -= 1
print('O resultado de {}! é {}, e a relação dos números é: {} '.format(lista_fatorial[0], resultado,lista_fatorial))