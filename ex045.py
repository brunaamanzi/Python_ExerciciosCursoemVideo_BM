# Crie um programa que faça o computador jogar Jokenpô com você (pedra, papel, tesoura).
print('-'*20)
print('Vamos jogar Jokenpô?')
print('-'*20)
import random
usuário = str(input('Escolha: pedra, papel ou tesoura? ')).lower()
print('JO')
from time import sleep
sleep(1)
print('KEN')
sleep(1)
print('PÔ!!!')
lista=['pedra','papel','tesoura']
computador = random.choice(lista)
print('*-'*20)
print('Eu escolhi: {}\nVocê escolheu: {}'.format(computador,usuário))
print('*-'*20)
if computador == 'pedra':
    if usuário == 'pedra':
        print('EMPATE!')
    elif usuário == 'papel':
        print('Você GANHOU!')
    elif usuário == 'tesoura':
        print('Você PERDEU!')
if computador == 'papel':
    if usuário == 'papel':
        print('EMPATE!')
    elif usuário == 'pedra':
        print('Você PERDEU!')
    elif usuário == 'tesoura':
        print('Você GANHOU!')
if computador == 'tesoura':
    if usuário == 'tesoura':
        print('EMPATE!')
    elif usuário == 'pedra':
        print('Você GANHOU!')
    elif usuário == 'papel':
        print('Você PERDEU!')
"""print('Empate! Eu também escolhi {}.'.format(computador))
elif usuário == 'pedra' and computador == 'papel':
    print('Você perdeu! Eu escolhi {}.'.format(computador))
elif usuário == 'pedra' and computador == 'tesoura':
    print('Você ganhou! Eu escolhi {}.'.format(computador))
elif usuário == 'papel' and computador == 'pedra':
    print('Você ganhou! Eu escolhi {}.'.format(computador))
elif usuário == 'papel' and computador == 'tesoura':
    print('Você perdeu! Eu escolhi {}.'.format(computador))
elif usuário == 'tesoura' and computador == 'pedra':
    print('Você perdeu! Eu escolhi {}.'.format(computador))
elif usuário == 'tesoura' and computador == 'papel':
    print('Você ganhou! Eu escolhi {}.'.format(computador))
else:
    print('não selecionada')"""
print('E aí, vamos jogar novamente? Basta pressionar Ctrl + Shift + F10.')