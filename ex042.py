# Refaça o Desafio 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# equilátero: todos os lados iguais
# isósceles: dois lados iguais
# escaleno: todos os lados diferentes

# ex035: desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
lado_1 = float(input('Insira o comprimento de um dos lados: '))
lado_2 = float(input('Insira o comprimento de mais um dos lados: '))
lado_3 = float(input('Insira o comprimento do outro lado: '))
if lado_1 < lado_2 + lado_3 and lado_2 < lado_1 + lado_3 and lado_3 < lado_1 + lado_2:
    print('Os segmentos informados podem formar um triângulo do tipo:')
    if lado_1 == lado_2 == lado_3:
        print('equilátero!')
    elif lado_1 != lado_2 != lado_3:
        print('escaleno!')
    else:
        print('isósceles!')
else:
    print('Os lados {}, {} e {} não podem formar um triângulo, pois o maior lado é maior ou igual à soma dos dois menores.'.format(lado_1,lado_2,lado_3))
