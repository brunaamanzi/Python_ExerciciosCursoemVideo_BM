"""Exercício 81: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
a) Quantos números foram digitados;
b) A lista de valores, ordenada de forma decrescente;
c) Se o valor 5 foi digitado e está ou não na lista."""
lista = []
while True:
    lista.append(int(input('Insira um número: ')))
    while True:
        continua = input('Deseja continuar? [S/N] ').lower().strip()[0]
        if continua in 'sn':
            break
    if continua == 'n':
        break
print('='*40)
print(f'Lista digitada: {lista}')
print(f'A lista possui {len(lista)} números.')
lista.sort(reverse=True)
print(f'Lista ordenada de forma decrescente: {lista}') # Não conseguimos imprimir a lista já ordenando pois primeiro precisamos ordenar para depois imprimir o resultado nesse caso.
if 5 in lista:
    print(f'O valor 5 foi digitado na posição {lista.index(5)}')
else:
    print('O valor 5 não está na lista.')
print('='*40)
