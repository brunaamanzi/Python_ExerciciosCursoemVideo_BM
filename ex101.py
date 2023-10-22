# Exercício 101: Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições.
from datetime import date
def voto(ano=0):
    ano_atual = date.today().year
    idade = ano_atual - ano
    print(f'Com {idade} anos: ',end='')
    if idade < 16:
        print('NÃO VOTA! ')
    elif 16 <= idade < 18 or idade >= 65:
        print('VOTO OPCIONAL!')
    else:
        print('VOTO OBRIGATÓRIO!')

nasc = int(input('Em que ano você nasceu? '))
voto(nasc)