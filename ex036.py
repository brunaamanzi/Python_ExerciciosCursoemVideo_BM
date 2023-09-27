# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar. Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.
from time import sleep
print('-'*60)
print('\033[1;34;40mBem vindo ao Banco Python! Vamos simular o seu financiamento?\033[m')
print('-'*60)
casa = float(input('\033[34mQual é o valor da casa que você deseja comprar? R$ '))
salario = float(input('Qual é o seu salário bruto mensal? R$ '))
prazo = float(input('Em quantos anos você deseja quitar seu financiamento? '))
prestação = casa / (prazo*12)
margem = salario*0.3
print('\033[1;34;40mCalculando...\033[m')
sleep(1)
print('\033[1;34;40mEnviando para aprovação...\033[m')
sleep(1)
print('\033[34mO valor da sua prestação vai ser de \033[1;34;40mR${:.2f}.\033[m'.format(prestação))
if prestação > margem:
    print('\033[31mInfelizmente seu financiamento não foi aprovado, pois sua margem é de R${:.2f}. Você pode tentar novamente com um prazo maior!'.format(margem))
elif prestação <= margem:
    print('\033[1;34;40mParabéns! Seu financiamento foi aprovado!\033[m')
print('\033[34mMuito obrigado por nos escolher!')


