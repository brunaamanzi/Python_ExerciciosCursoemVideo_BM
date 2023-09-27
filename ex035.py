# desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
lado_1 = float(input('Insira o comprimento de um dos lados: '))
lado_2 = float(input('Insira o comprimento de mais um dos lados: '))
lado_3 = float(input('Insira o comprimento do outro lado: '))
lista = [lado_3,lado_2,lado_1]
lista_ordem = sorted(lista)
if lista_ordem[-1] < lista_ordem[0] + lista_ordem[1]:
    print('Os lados {}, {} e {} podem formar um triângulo!'.format(lado_1,lado_2,lado_3))
else:
    print('Os lados {}, {} e {} não podem formar um triângulo, pois o maior lado é maior do que a soma dos dois menores.'.format(lado_1,lado_2,lado_3))
