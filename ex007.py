#Desafio 07: Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.
nota_1 = float(input('Nota 1 do Aluno: '))
nota_2 = float(input('Nota 2 do Aluno: '))
print('As notas do Aluno foram {:.1f} e {:.1f}, e sua média ficou {:.1f}.'.format(nota_1,nota_2,(nota_1+nota_2)/2))