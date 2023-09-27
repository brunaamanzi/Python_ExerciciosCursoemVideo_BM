# Crie um programa que leia uma frase e mostre:

frase=str(input('Escreva uma frase: ')).lower().strip()
# o .lower() no final transforma a string em letras minúsculas e grava dessa forma

print('A letra "a" aparece {} vezes.'.format(frase.count('a')))
print('A primeira vez que a letra "a" aparece é na posiçao {}'.format(frase.find('a')+1))
print('A última vez que a letra "a" aparece é na posição {}.'.format(frase.rfind('a')+1))
print('O tamanho da frase é {}'.format(len(frase)))