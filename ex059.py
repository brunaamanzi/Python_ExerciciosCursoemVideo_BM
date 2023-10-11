""" 59: Crie um programa que leia dois valores e mostre um menu na tela:
[1] SOMAR
[2] MULTIPLICAR
[3] MAIOR
[4] NOVOS NÚMEROS
[5] SAIR DO PROGRAMA
Seu programa deverá realizar a operação solicitada em cada caso."""
lista_num = []
lista_num_1 = []
for c in range (1,3):
    num = int(input('Insira o {}º número: '.format(c)))
    lista_num.append(num)
opção_desejada = 0
opção_desejada_1 = 0
while opção_desejada == 0:
    opção = int(input('[1] soma\n[2] multiplicação\n[3] retornar o maior\n[4] inserir novos números\n[5] sair do programa\nSelecione a sua operação desejada: '))
    if opção in (1,2,3,4,5):
        opção_desejada += opção
if opção_desejada == 1:
    soma = sum(lista_num)
    print(soma)
elif opção_desejada == 2:
    multiplicação = lista_num[0]*lista_num[-1]
    print(multiplicação)
elif opção_desejada == 3:
    lista_num.sort()
    print(lista_num[-1])
elif opção_desejada == 4:
    for c in range(1, 3):
        num_1 = int(input('Insira o {}º número: '.format(c)))
        lista_num_1.append(num_1)
elif opção_desejada == 5:
    print('Programa Encerrado!')
