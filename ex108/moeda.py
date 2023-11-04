def aumentar(n = 0,p = 0): # estamos criando parâmetros opcionais
    res = n+(n*p/100)
    return res

def diminuir(n = 0,p = 0):
    res = n-(n*p/100)
    return res

def dobro(n = 0):
    res = n * 2
    return res

def metade(n = 0):
    res = n / 2
    return res

def moeda (p = 0,m = 'R$'):
    return f"{m}{p:.2f}".replace(".",",")
