# 57: Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores "M" ou "F". Caso esteja errado, peça a digitação novamente até ter um valor correto.
sexo = input('Insira o seu sexo [F/M]: ').upper().strip()
while sexo not in 'FM': # OR: while s not in 'FM':
    sexo = input('Dados inválidos. Insira o seu sexo [F/M]: ').upper().strip()[0]
print('Sexo registrado com sucesso')