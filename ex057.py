# 57: Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores "M" ou "F". Caso esteja errado, peça a digitação novamente até ter um valor correto.
s = ''
while s != 'F' and s != 'M':
    sexo = input('Insira o sexo de uma pessoa [F/M]: ')
    if sexo == 'F' or sexo == 'M':
        s += sexo
print('O sexo informado foi: {}'.format(s))