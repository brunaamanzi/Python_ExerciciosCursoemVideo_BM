# Exercício 83: Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.
expressão = str(input('Digite sua expressão: '))
verif = []
for cont in expressão:
    if cont == "(":
        verif.append("(")
    elif cont == ")":
        if len(verif) > 0:
            verif.pop()
        else:
            verif.append(")")
            break
if len(verif)== 0:
    print('Sua expressão está correta!')
else:
    print('Sua expressão está errada.')
