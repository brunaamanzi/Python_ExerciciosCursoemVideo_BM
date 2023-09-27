# Desafio 4: Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações
# possíveis sobre ele.
texto=input('Digite algo: ')
print('O tipo primitivo desse valor é ',type(texto))
print('Só tem números? ',texto.isnumeric())
print('Está em letra minúscula? ',texto.islower())
print('Só tem espaços?',texto.isspace())
print('Possui números decimais?',texto.isdecimal())
print('Está capitalizada? (primeira letra maiúscula)',texto.istitle())

