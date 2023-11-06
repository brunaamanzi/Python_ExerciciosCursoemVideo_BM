# Exercício Python 113: Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um número de tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.

def leiaInt(txt):
    while True:
        a = ''
        try:
            a = int(input(txt))
            return a
        except ValueError:
            print('\033[1;31mERRO! Digite um número inteiro válido.\033[m')
        except KeyboardInterrupt:
            print('\033[1;31m\nO usuário preferiu não digitar esse número.\033[m')
            return 0
        if a.isnumeric():
            break
def leiaFloat(txt):
    while True:
        b = ''
        try:
            b = float(input(txt))
            return b
        except ValueError:
            print(f'\033[1;31mERRO! Digite um número real válido.\033[m')
        except KeyboardInterrupt:
            print('\033[1;31m\nO usuário preferiu não digitar esse número.\033[m')
            return 0
        if b.isnumeric():
            break

i = leiaInt('Digite um número inteiro: ')
r = leiaFloat('Digite um número Real: ')
print(f'O valor inteiro digitado foi {i} e o real foi {r}')