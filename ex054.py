# 54: Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
from datetime import date
ano_atual = date.today().year
maioridade = []
for i in range (0,7):
    ano_nascimento = int(input('Escreva seu ano de nascimento: '))
    idade = ano_atual - ano_nascimento
    if idade >= 18:
        maioridade.append(1)
total_maioridade = sum(maioridade)
total_menor = 7 - total_maioridade
print('Nº de pessoas que já atingiu a maioridade: {}\nNº de pessoas que são "de menor": {}.'.format(total_maioridade,total_menor))

