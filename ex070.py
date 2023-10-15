"""Exercício 70: Crie um programa que leia o preço e o nome de vários produtos. O programa deverá perguntar se o usuário vai continuar. No final, mostre:
a) qual é o total gasto na compra;
b) quantos produtos custam mais de R$1.000,00;
c) qual é o nome do produto mais barato."""
total_gasto = produto_mais_barato = menor_preço = cont_prod_mais_1000 = 0
continua = ' '
while True:
    produto = input('Produto: ')
    preço = float(input('Preço: R$'))
    total_gasto += preço
    if preço > 1000:
        cont_prod_mais_1000 += 1
    if menor_preço == 0:
        menor_preço = preço
        produto_mais_barato = produto
    if preço < menor_preço:
        menor_preço = preço
        produto_mais_barato = produto
    continua = input('Deseja continuar? [S/N] ').lower().strip()[0]
    while continua not in 'sn':
        continua = input('Deseja continuar? [S/N] ').lower().strip()[0]
    if continua in 'n':
        break
print('{:^60}'.format('PROGRAMA ENCERRADO'))
print('-*'*30)
print(f'\033[1;32mO total gasto foi R${total_gasto:.2f}\nA quantidade de itens acima de R$1.000,00 foi: {cont_prod_mais_1000}.\nO produto mais barato foi {produto_mais_barato}, que custa R${menor_preço:.2f}\033[m')
print('-*'*30)

