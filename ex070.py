"""Exercício 70: Crie um programa que leia o preço e o nome de vários produtos. O programa deverá perguntar se o usuário vai continuar. No final, mostre:
a) qual é o total gasto na compra;
b) quantos produtos custam mais de R$1.000,00;
c) qual é o nome do produto mais barato."""
total_gasto = 0
produtos_mais_1000 = 0
produto_mais_barato = 0
cont_prod_mais_1000 = 0
while True:
    produto = input('Nome do Produto: ')
    preço = float(input('Preço do Produto: R$'))
    continua = input('Deseja continuar? [S/N] ').lower().strip()
    total_gasto += preço
    produto_mais_barato = produto
    menor_preço = preço
    if preço > 1000:
        produtos_mais_1000 += preço
        cont_prod_mais_1000 += 1
    if preço < menor_preço:
        menor_preço = preço
        produto_mais_barato = produto
    if continua in 'sn':
        if continua == 'n':
            break
    else:
        continua = input('Deseja continuar? [S/N] ').lower().strip()
print(f'O total gasto foi R${total_gasto:.2f}, a quantidade de itens acima de R$1.000,00 foi: {cont_prod_mais_1000} e o produto mais barato foi {produto_mais_barato}.')

