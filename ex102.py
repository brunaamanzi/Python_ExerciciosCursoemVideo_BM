# Exercício 102: Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a calcular e o outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.
def fatorial(num,show=False):
    """
    Calcula o fatorial de um número.
    :param num: o número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta.
    :return: o valor do fatorial de um número num.
    """
    f = 1
    for c in range (num,0,-1):
        f *= c
        if show:
            if c > 1:
                print(c,end=' x ')
            else:
                print(c,end=' = ')
    print(f)

help(fatorial)
num=int(input('Digite um número: '))
fatorial(num,show=True)
num=int(input('Digite um número: '))
fatorial(num,show=False)
num=int(input('Digite um número: '))
fatorial(num)
