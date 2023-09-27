# Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
# 1 para binário
# 2 para octal
# 3 para hexadecimal
numero = int(input('Insira um número inteiro qualquer: '))
print('Selecione a base para conversão:\n1: converter para binário\n2: converter para octal\n3: converter para hexadecimal')
conversão = int(input('Escolha uma das bases acima para conversão: '))
if conversão == 1:
    print('{} convertido para binário, é: {}.'.format(numero,bin(numero)[2:]))
elif conversão == 2:
    print('{} convertido para octal, é: {}.'.format(numero,oct(numero)[2:]))
elif conversão == 3:
    print('{} convertido para hexadecimal, é: {}'.format(numero,hex(numero)[2:]))
else:
    print('Opção inválida.')


