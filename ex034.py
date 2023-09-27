# escreva um programa que pergunte o salário de um funcionário e calcule o valor de seu aumento.
# para salários superiores à R$1.250,00, calcule um aumento de 10%.
# para os inferiores ou iguais, o aumento é de 15%.
salario = float(input('Informe o seu salário: '))
if salario > 1250:
    print('Seu salário receberá aumento de 10% e passará a ser de R${:.2f}.'.format(salario*1.1))
else:
    print('Seu salário receberá aumento de 15% e passará a ser de R${:.2f}.'.format(salario*1.15))

