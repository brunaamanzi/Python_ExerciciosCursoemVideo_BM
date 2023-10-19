# Exercício 89: Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.
lista_alunos = []
nome = []
nota = []
continua = ''
boletim = ''
while True:
    print('-'*30)
    nome.append(input('Nome do Aluno: ').capitalize())
    nota.append(float(input('1ª Nota do aluno: ')))
    nota.append(float(input('2ª Nota do aluno: ')))
    print('-'*30)
    nome.append(nota[:])
    lista_alunos.append(nome[:])
    nome.clear()
    nota.clear()
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
    print(f'{i:<3}{c[0]:<15}{(c[1][0]+c[1][1])/2:>5}')
print('='*35)
while True:
    boletim = int(input('Você deseja ver as notas de qual aluno? (999 interrompe): '))
    print(f'As notas de {lista_alunos[boletim][0]} são: {lista_alunos[boletim][1]}')
    print('-'*30)
    if boletim == 999:
        break
print('THE END')
