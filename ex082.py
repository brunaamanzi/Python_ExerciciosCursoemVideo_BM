# Exercício 82: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.
lista_total = []
lista_pares = []
lista_impares = []
while True:
    lista_total.append(int(input('Insira um número: ')))
    while True:
        continua = input('Deseja continuar? [S/N] ').lower().strip()[0]
        if continua in 'sn':
            break
    if continua == 'n':
        break
for valor in lista_total:
    if valor % 2 == 0:
        lista_pares.append(valor)
    else:
        lista_impares.append(valor)
print('-'*40)
print(f'A lista completa é {lista_total}')
print(f'A lista que contém os números pares é: {lista_pares}')
print(f'A lista que contém os números ímpares é: {lista_impares}')
print('-'*40)
