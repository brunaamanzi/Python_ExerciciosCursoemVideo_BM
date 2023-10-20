"""Exercício 94: Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre:
a) quantas pessoas foram cadastradas;
b) a média de idade do grupo;
c) uma lista com todas as mulheres;
d) uma lista com todas as pessoas com idade acima da média."""
lista_todos = []
info = {}
idade = 0
while True:
    info['nome']=input('Insira o nome: ')
    info['sexo']=input('Insira o sexo: [F/M] ').lower().strip()[0]
    info['idade']=int(input('Insira a idade: '))
    idade += info['idade']
    lista_todos.append(info.copy())
    while True:
        continua = input('Deseja continuar? [S/N] ').lower().strip()[0]
        if continua in 'sn':
            break
    if continua == 'n':
        break
print('-'*40)
print(f'- O grupo tem {len(lista_todos)} pessoas.')
média_idade = idade / len(lista_todos)
print(f'- A média de idade é de {média_idade:.0f} anos.')
print(f'- As mulheres cadastradas foram: ',end='')
for p in lista_todos: # iremos percorrer uma lista, não precisa de .items()
    for k,v in p.items():
        if k == 'sexo' and v == 'f':
            print(f'[{p["nome"]}] ',end='')
print()
print('- Lista das pessoas que estão acima da média: ')
for p in lista_todos:
    if p['idade'] > média_idade:
        print(p)
print('<< ENCERRADO >>')