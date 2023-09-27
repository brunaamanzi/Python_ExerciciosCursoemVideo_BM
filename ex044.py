# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# à vista dinheiro/cheque: 10% de desconto
# à vista no cartão de débito: 5% de desconto
# em até 2x no cartão de crédito: preço normal
# 3x ou mais no cartão de crédito: 20% de juros
import time
print('-'*58)
print('\033[1;30;45mOlá! Bem vindo(a) à Mercearia do Bairro! Vamos às compras?\033[m')
print('-'*58)
time.sleep(1)
print('\033[1;35mFormas de pagamento:\033[m\nà vista (\033[1;35mdinheiro\033[m/\033[1;35mcheque\033[m): \033[1m10% de desconto\033[m\nà vista no \033[1;35mcartão de débito\033[m/: \033[1m5% de desconto\033[m\nem até \033[1;35m2x no cartão de crédito\033[m: \033[1mpreço normal\033[m\n\033[1;35m3x ou mais no cartão de crédito\033[m: \033[1m20% de juros\033[m')
time.sleep(1)
produto = input('\033[1;32mInsira o produto escolhido: ')
time.sleep(1)
valor = float(input('Insira o valor a ser pago: \033[m'))
time.sleep(1)
forma_pagamento = input('\033[1;32mEscolha sua forma de pagamento (\033[4;32mdinheiro\033[32m/\033[4;32mcheque\033[32m/\033[4;32mcartão de débito\033[32m/\033[4;32mcartão de crédito\033[m\033[32m):\033[m ').lower()
time.sleep(1)
if forma_pagamento == 'cartão de crédito':
    parcelas = int(input('\033[1;32mInsira o número de parcelas desejadas: \033[m'))
# aqui começamos uma nova condição
if forma_pagamento == 'dinheiro' or forma_pagamento == 'cheque':
    print('Você ganhou 10% de desconto! O valor a ser pago é: R${:.2f}.'.format(valor*0.9))
elif forma_pagamento == 'cartão de débito':
    print('Você ganhou 5% de desconto! O valor a ser pago é: R${:.2f}'.format(valor*0.95))
elif forma_pagamento == 'cartão de crédito':
    if parcelas == 1 or parcelas == 2:
        print('O valor a ser pago é: R${:.2f}'.format(valor))
    elif parcelas > 2:
        print('Para {} parcelas, você pagará 20% de juros. O valor a ser pago é: R${:.2f}'.format(parcelas,valor*1.2))
time.sleep(1)
print('{:*^50}'.format(' Agradecemos a sua visita! Volte sempre. '))