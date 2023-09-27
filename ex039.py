# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
# Se ele ainda vai se alistar ao serviço militar;
# Se é a hora de se alistar;
# Se já passou do tempo do alistamento;
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
from datetime import date
ano_atual = date.today().year
print('-'*50)
print('\033[1;30;44mOlá! Seja muito bem vindo. Vamos verificar seu status de alistamento militar?\033[m')
print('-'*50)
sexo = input('Informe seu sexo (feminino/masculino): ').lower()
ano_nascimento = int(input('Insira seu ano de nascimento: '))
idade = ano_atual - ano_nascimento
if sexo == 'masculino':
    print('Nasceu em {}, tem {} anos em {}.'.format(ano_nascimento,idade,ano_atual))
elif sexo == 'feminino':
    print('Você não precisa se alistar.')
if idade == 18 and sexo == 'masculino':
    print('\033[1;34mVocê está sendo convocado! É hora de se alistar ao serviço militar!\033[m')
elif idade > 18 and sexo == 'masculino':
    print('\033[1;31mURGENTE!!!\nVocê deveria ter se alistado há {} ano(s), em {}. Procure a unidade mais próxima e regularize sua situação o quanto antes.\033[m'.format(idade-18,ano_nascimento+18))
elif idade < 18and sexo == 'masculino':
    print('Você ainda não atingiu 18 anos. Volte para se alistar daqui a {} ano(s), em {}.'.format((idade-18)*(-1),ano_nascimento+18))
