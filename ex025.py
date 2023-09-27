# Crie um programa que leia o nome de uma pessoa e diga se ela tem "Silva" no nome:
nome=input('Escreva seu nome: ').strip().lower()
#print('Silva' in nome)
print('Seu nome tem Silva? {}'.format('silva' in nome))