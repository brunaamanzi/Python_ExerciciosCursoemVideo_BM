# Exercício 104: Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante à função input do Python, só que fazendo a validação para aceitar apenas um valor numérico inteiro.
# Exemplo:
# n = leiaInt('Digite um número: ')

def leiaInt(txt=0):
   while True:
        a = ''
        try:
            a = int(input(txt))
            return a
        except ValueError:
            print('\033[1;31mERRO! Digite um número inteiro válido.\033[m')
        if a.isnumeric():
            break
n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}!')



