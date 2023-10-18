# Exercício 83: Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.
lista = []
expressão = str(input('Digite sua expressão: '))
abrindo = expressão.count('(')
fechando = expressão.count(')')
lista.append(abrindo)
lista.append(fechando)
if lista[0] == lista[1]:
    print('Sua expressão está correta!')
else:
    print('Sua expressão está errada.')
