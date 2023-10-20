# Exercício 89: Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.
lista_alunos = []
while True:
    print('-'*30)
    nome = input('Nome do Aluno: ').capitalize()
    nota1 = float(input(f'1ª Nota de {nome}: '))
    nota2 = float(input(f'2ª Nota de {nome}: '))
    média = (nota1 + nota2) / 2
    lista_alunos.append([nome,[nota1,nota2],média])
    print('-'*30)
    while True:
        continua = input('Deseja continuar? [S/N] ').lower().strip()[0]
        if continua in 'sn':
            break
    if continua == 'n':
        break
print('='*35)
print(f'{"Nº":<3}{"NOME":<15}{"MÉDIA":>5}')
print('-'*35)
for i, c in enumerate(lista_alunos):
    print(f'{i:<3}{c[0]:<15}{c[2]:>5.1f}')
print('='*35)
while True:
    boletim = int(input('Você deseja ver as notas de qual aluno? (999 interrompe): '))
    if boletim == 999:
        break
    if 0 <= boletim < len(lista_alunos):
        print(f'As notas de {lista_alunos[boletim][0]} são: {lista_alunos[boletim][1]}')
    else:
        print('Aluno não encontrado. Tente novamente.')
    print('-'*30)
print('THE END')
