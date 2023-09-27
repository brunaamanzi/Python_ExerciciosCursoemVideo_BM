# Desafio 20: O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
import random
aluno1=input('Insira o nome do 1º aluno: ')
aluno2=input('Insira o nome do 2º aluno: ')
aluno3=input('Insira o nome do 3º aluno: ')
aluno4=input('Insira o nome do 4º aluno: ')
lista=[aluno3,aluno4,aluno1,aluno2]
random.shuffle(lista)
print('A ordem de apresentação dos trabalhos será:\n{}'.format(lista))
