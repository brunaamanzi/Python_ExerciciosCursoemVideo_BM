def aumentar(n = 0,p = 0,formato=False): # estamos criando parâmetros opcionais
    """
    Essa função é utilizada para realizar aumentos em %.
    :param n: Valor a ser calculado
    :param p: percentual
    :param formato: para formatar com vírgula e duas casas decimais (quando True)
    :return: para imprimir o resultado do cálculo com a formatação
    """
    res = n+(n*p/100)
    return res if formato is False else moeda(res)
    # outra opção:
    # return res if not formato else moeda(res)

def diminuir(n = 0,p = 0,formato=False):
    """
    Essa função é utilizada para realizar reduções em %.
    :param n: Valor a ser calculado
    :param p: percentual
    :param formato: para formatar com vírgula e duas casas decimais (quando True)
    :return: para imprimir o resultado do cálculo com a formatação
    """
    res = n-(n*p/100)
    return res if formato is False else moeda(res)

def dobro(n = 0,formato=False):
    """
    Função para calcular o dobro do valor informado.
    :param n: valor a ser calculado
    :param formato: para formatar com vírgula e duas casas decimais (quando true)
    :return: para imprimir o resultado do cálculo com a formação
    """
    res = n * 2
    return res if formato is False else moeda(res)

def metade(n = 0,formato=False):
    """
    Função para calcular a metade do valor informado.
    :param n: valor a ser calculado
    :param formato: para formatar com vírgula e duas casas decimais (quando true)
    :return: para imprimir o resultado do cálculo com a formação
    """
    res = n / 2
    return res if formato is False else moeda(res)

def moeda (p = 0,m = 'R$'):
    """
    Essa função serve para formatar a moeda com duas casas decimais, considerando o valor com vírgulas sem dar erro no cálculo (Python só aceita valores com separador em ponto)
    :param p: valor
    :param m: moeda (R$, US$...)
    :return: imprime o resultado na formatação desejada
    """
    return f"{m}{p:.2f}".replace(".",",") # para formatar com vírgula, e não com ponto

def ajuda(função):
    help(função)

def resumo(p = 0,a = 0,r = 0):
    print('-'*40)
    print(f'{"RESUMO DO VALOR":^40}')
    print('-'*40)
    print(f'{"Preço analisado:":<30} {moeda(p)}')
    print(f'{"Dobro do preço:":<30} {moeda(p*2)}')
    print(f'{"Metade do preço:":<30} {moeda(p/2)}')
    print(f'{a:2}{"% de aumento:":<28} {moeda(p+(p*a/100))}')
    print(f'{r:2}{"% de redução:":<28} {moeda(p-(p*r/100))}')
    print('-'*40)

