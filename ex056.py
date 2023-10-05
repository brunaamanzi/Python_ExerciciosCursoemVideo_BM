# 56: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: A média de idade do grupo, Qual é o nome do homem mais velho, Quantas mulheres tem menos de 20 anos.
 = []
for i in range (0,4):
    nome = str(input('Insira seu nome: ')).capitalize()
    idade = str(input('Insira sua idade: '))
    sexo = str(input('Insira seu sexo (feminimo/masculino): ')).lower()
