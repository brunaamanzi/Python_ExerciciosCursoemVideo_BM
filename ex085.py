# Exercício 85: Crie um programa onde o usuário possa digitar 7 valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.
numeros = [[],[]]
for c in range (0,7):
    num = int(input('Insira um número: '))
    if num % 2 == 0:
        numeros[0].append(num)
    else:
        numeros[1].append(num)
numeros[0].sort()
numeros[1].sort()
print('-'*60)
print(f'Os valores \033[1;34mpares\033[m digitados foram: \033[1;34m{numeros[0]}\033[m')
print(f'Os valores \033[1;34mímpares\033[m digitados foram: \033[1;34m{numeros[1]}\033[m')
print('-'*60)
