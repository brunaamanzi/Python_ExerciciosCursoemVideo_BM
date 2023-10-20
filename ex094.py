"""Exercício 94: Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre:
a) quantas pessoas foram cadastradas;
b) a média de idade do grupo;
c) uma lista com todas as mulheres;
d) uma lista com todas as pessoas com idade acima da média."""
lista_todos = []
info = {}
idade = média_idade = 0
while True:
    info['nome']=input('Insira o nome: ')
    while True:
        info['sexo']=input('Insira o sexo: [F/M] ').upper().strip()[0]
        if info['sexo'] in 'FM':
            break
        print('ERRO! Por favor, escolha F/M: ')
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
print(f'- Ao todo temos {len(lista_todos)} pessoas cadastradas.')
média_idade = idade / len(lista_todos)
print(f'- A média de idade é de {média_idade:.0f} anos.')
print(f'- As mulheres cadastradas foram: ',end='')
for p in lista_todos: # iremos percorrer uma lista, não precisa de .items()
    if p["sexo"] == 'F': # nesse caso, não precisamos utilizar o k,v, pois podemos chamar com p['sexo']
        print(f'[{p["nome"]}] ',end='')
""" for k,v in p.items(): # essa forma também está correta
        if k == 'sexo' and v == 'f':"""
print()
print('- Lista das pessoas que estão acima da média: ')
for p in lista_todos:
    if p['idade'] > média_idade:
        for k,v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print('<< ENCERRADO >>')