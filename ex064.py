"""64: Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o 999)."""
print('Olá! Bem vindo ao nosso Somatório.\nInsira quantos números você quiser e iremos realizar a soma entre eles. Para encerrar, digite 999.')
lista = []
num = 0
num = int(input("Insira um número: "))
while num != 999:
    lista.append(num)
    num = int(input("Insira um número: "))
print('Você escreveu {} números e a soma entre eles é {}.\nVeja abaixo a relação dos números que foram somados: {}'.format(len(lista),sum(lista),lista))
