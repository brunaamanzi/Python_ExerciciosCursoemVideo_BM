# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
nome_completo=input('Escreva o seu nome completo: ').strip()
nome_lista=nome_completo.split()
print("Primeiro Nome:\n{}".format(nome_lista[0]))
print("Último Nome:\n{}".format(nome_lista[-1]))