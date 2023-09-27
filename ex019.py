#Desafio 19: um professor quer sortear um dos quatro alunos para apagar o quadro. faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.
from random import choice
aluno1=input('Insira o nome do 1º aluno: ')
aluno2=input('Insira o nome do 2º aluno: ')
aluno3=input('Insira o nome do 3º aluno: ')
aluno4=input('Insira o nome do 4º aluno: ')
lista=[aluno4,aluno3,aluno2,aluno1]
sorteio=choice(lista)
print('SORTEIO')
print('O aluno sorteado para apagar o quadro foi {}.'.format(sorteio))
