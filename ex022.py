# Exercício 22: crie um programa que leia o nome completo da pessoa e mostre: nome com todas as letras maiúsculas,
# todas as letras minúsculas, quantas letras ao todo (sem considerar espaços), quantas letras tem o primeiro nome.
nome = input('Escreva o seu nome: ').strip()
print("analisando seu nome...")
print("em letras maiúsculas: {}".format(nome.upper()))
print("em letras minúsculas: {}".format(nome.lower()))
#nome_junto=nome.replace(' ','')
print("quantidade de caracteres: {}".format(len(nome)-nome.count(' ')))
nome_lista=nome.split()
print('o primeiro nome é {} e tem {} letras.'.format(nome_lista[0],len(nome_lista[0])))