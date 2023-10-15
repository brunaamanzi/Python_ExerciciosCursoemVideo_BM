# Exercício 66: Crie um programa que leia vários números inteiros pelo teclado. O Programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).
cont = soma = num = 0
while True:
    num = int(input("Insira um número: "))
    if num == 999:
        break
    soma += num
    cont += 1
print(f'Você escreveu {cont} números e a soma entre eles é {soma}.')