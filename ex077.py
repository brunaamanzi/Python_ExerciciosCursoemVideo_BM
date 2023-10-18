# Exercício 77: Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
lista_palavras = ('APRENDER','PROGRAMAR','LINGUAGEM','PYTHON','CURSO','GRATIS','ESTUDAR','PRATICAR','TRABALHAR','MERCADO','PROGRAMADOR','FUTURO')
for palavra in lista_palavras:
    print(f'\nNa palavra {palavra} temos:',end=' ')
    if 'A' in palavra:
        print('a',end=' ')
    if 'E' in palavra:
        print('e',end=' ')
    if 'I' in palavra:
        print('i',end=' ')
    if 'O' in palavra:
        print('o',end=' ')
    if 'U' in palavra:
        print('u',end=' ')
print('\nfim')