# Exercício 102: Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a calcular e o outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.
def fatorial(num,show=False):
    f = 1
    n = num
    for c in range (num,0,-1):
        f *= c
    if True:
        while n >= 1:
            if n > 1:
                print(n,end=' x ')
            else:
                print(n,end='')
            n -= 1
    print(f' = {f}',end='')
    print()
    if False:
        return f

num=int(input('Digite um número: '))
fatorial(num,show=True)
num=int(input('Digite um número: '))
fatorial(num,show=False)
