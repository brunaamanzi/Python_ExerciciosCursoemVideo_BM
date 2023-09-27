# Exercício 05: Escreva um programa que pergunte a quantidade de KM percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por KM rodado.
km_percorrido = float(input('Informe a quantidade de KM percorridos: '))
dias_aluguel = int(input('Informe a quantidade de dias em que o carro foi alugado: '))
print('-'*15)
print('O preço do aluguel é R$60 por dia e o valor do KM rodado é R$0.15.\nKM percorrido: {}\nPeríodo de aluguel: {}\nO preço a pagar é R${:.2f}'.format(km_percorrido,dias_aluguel,(60*dias_aluguel)+(0.15*km_percorrido)))