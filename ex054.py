# 54: Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
from datetime import date
ano_atual = date.today().year
maioridade = 0
menoridade = 0
for i in range (0,7):
    ano_nascimento = int(input('{} Escreva seu ano de nascimento: '.format(i+1)))
    idade = ano_atual - ano_nascimento
    if idade >= 18:
        maioridade += 1
    else:
        menoridade += 1
print('Nº de pessoas que já atingiu a maioridade: {}\nNº de pessoas que são "de menor": {}.'.format(maioridade,menoridade))

