# Outra opção para o exercício 103:
def ficha(n='', g=0):
    try:
        n = input('Nome do jogador: ')
        g = int(input('Número de gols: '))
    except ValueError:
        n = '<desconhecido>'
        g = 0
    print(f'O jogador {n} fez {g} gol(s).')


ficha()