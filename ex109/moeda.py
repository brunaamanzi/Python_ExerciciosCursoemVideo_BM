def aumentar(n = 0,p = 0,formato=False): # estamos criando parâmetros opcionais
    res = n+(n*p/100)
    return res if formato is False else moeda(res)
    # outra opção:
    # return res if not formato else moeda(res)

def diminuir(n = 0,p = 0,formato=False):
    res = n-(n*p/100)
    return res if formato is False else moeda(res)

def dobro(n = 0,formato=False):
    res = n * 2
    return res if formato is False else moeda(res)

def metade(n = 0,formato=False):
    res = n / 2
    return res if formato is False else moeda(res)

def moeda (p = 0,m = 'R$'):
    return f"{m}{p:.2f}".replace(".",",") # para formatar com vírgula, e não com ponto
