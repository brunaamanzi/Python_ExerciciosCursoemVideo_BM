# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "Santo":
cidade=input('Escreva o nome de uma cidade: ').strip().lower()
# cidade_separado = cidade.split()
# print("santo" in cidade_separado[0])
print(cidade[:5] == "santo")