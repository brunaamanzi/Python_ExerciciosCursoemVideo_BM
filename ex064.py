# 64: Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o 999).
lista = []
num = 0
while num != 999:
    num = int(input("Insira um número: "))
    lista.append(num)
lista.remove(999)
print('Você escreveu {} números e a soma entre eles é {}'.format(len(lista),sum(lista)))
print(lista)