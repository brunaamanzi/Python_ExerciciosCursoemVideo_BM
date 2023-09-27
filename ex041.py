# A confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
# até 9 anos: MIRIM
# até 14 anos: INFANTIL
# até 19 anos: JUNIOR
# até 20 anos: SENIOR
# acima de 20 anos: MASTER
print('\033[1;34;40mBem vindo à Confederação Nacional de Natação!\033[m')
ano_nascimento = int(input('Insira seu ano de nascimento: '))
from datetime import date
ano_atual = date.today().year
idade = ano_atual - ano_nascimento
if idade <= 9:
    print('\033[1mSua idade é {} anos e sua categoria é: MIRIM'.format(idade))
elif 9 < idade <= 14:
    print('Sua idade é {} anos e sua categoria é: INFANTIL'.format(idade))
elif 14 < idade <= 19:
    print('Sua idade é {} anos e sua categoria é: JUNIOR'.format(idade))
elif 19 < idade <= 20:
    print('Sua idade é {} anos e sua categoria é: SENIOR'.format(idade))
elif idade > 20:
    print('Sua idade é {} anos e sua categoria é: MASTER'.format(idade))
