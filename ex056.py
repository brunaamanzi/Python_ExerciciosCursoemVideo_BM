# 56: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: A média de idade do grupo, Qual é o nome do homem mais velho, Quantas mulheres tem menos de 20 anos.
total_idade = 0
nome_homem_velho = ""
idade_homem_velho = 0
mulheres_menos_20 = 0
for i in range (1,5):
    print('----- {}ª PESSOA ----- '.format(i))
    nome = str(input('Insira seu nome: ')).capitalize()
    idade = int(input('Insira sua idade: '))
    sexo = str(input('Insira seu sexo (f/m): ')).lower()
    total_idade += idade
    if sexo == 'm' and idade > idade_homem_velho:
        idade_homem_velho = idade
        nome_homem_velho = nome
    if sexo == 'f' and idade < 20:
        mulheres_menos_20 += 1
média_idade = total_idade / 4
print('-*'*20)
print('A média de idade é {} anos.'.format(média_idade))
if idade_homem_velho > 0:
    print('O nome do homem mais velho é {} e sua idade é {}.'.format(nome_homem_velho,idade_homem_velho))
else:
    print('Não tem homens na lista.')
print('O número de mulheres com menos de 20 anos é: {}'.format(mulheres_menos_20))