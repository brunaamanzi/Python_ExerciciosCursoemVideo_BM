# Exercício 71: Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
# OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
print('='*40)
print('{:^39}'.format('BANCO PYTHON'))
print('=' * 40)
sacado = cedulas_50 = cedulas_20 = cedulas_10 = cedulas_1 = 0
saque = int(input('Qual valor você deseja sacar? R$ '))
while True:
    saldo = saque - sacado
    if saldo == 0:
        break
    if saldo - 50 >= 0:
        cedulas_50 += 1
        sacado += 50
    elif saldo - 20 >= 0:
        cedulas_20 += 1
        sacado += 20
    elif saldo - 10 >= 0:
        cedulas_10 += 1
        sacado += 10
    elif saldo - 1 >= 0:
        cedulas_1 += 1
        sacado += 1
print(f'{cedulas_50} cédulas de R$50,00\n{cedulas_20} cédulas de R$20,00\n{cedulas_10} cédulas de R$10,00\n{cedulas_1} cédulas de R$1,00')
print('='*40)
print('Volte Sempre!')