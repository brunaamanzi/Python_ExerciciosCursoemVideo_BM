# Outra forma de resolver o exercício 104:

def leiaInt(txt):
    ok = False
    valor = 0
    while True:
        n = str(input(txt))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[1;31mErro! Digite um número inteiro válido.\033[m')
        if ok:
            break
    return valor

n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')