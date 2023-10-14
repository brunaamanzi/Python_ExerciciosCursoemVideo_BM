# Exercício 68: Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador PERDER, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
print('-*'*20)
print('{:^40}'.format('Vamos jogar PAR ou ÍMPAR!'))
print('-*'*20)
import random
computador = random.randint(0,10)
jogador = 0
vitória = 0
derrota = 0
while True:
    jogador = int(input('Digite um valor: '))
    resultado = computador + jogador
    opção = str(input('PAR ou ÍMPAR? [P/I] ')).lower().strip()[0]
    print(f'Você jogou {jogador} e o computador {computador}. \033[1;36mResultado: {resultado}\033[m -> ',end=' ')
    if resultado % 2 == 0:
        print('PAR')
    else:
        print('ÍMPAR')
    if opção == 'p':
        if resultado % 2 == 0:
            print('--'*20)
            print('\033[1;32mVocê VENCEU! Vamos jogar novamente...\033[m')
            print('--'*20)
            vitória += 1
        else:
            print('--'*20)
            print('\033[1;31mVocê PERDEU!\033[m')
            print('--'*20)
            derrota += 1
    if opção == 'i':
        if resultado % 2 != 0:
            print('--' * 20)
            print('\033[1;32mVocê VENCEU! Vamos jogar novamente...\033[m')
            print('--' * 20)
            vitória += 1
        else:
            print('--' * 20)
            print('\033[1;31mVocê PERDEU!\033[m')
            print('--' * 20)
            derrota += 1
    if derrota > 0:
        break
print(f'GAME OVER! Você venceu {vitória} vezes.')