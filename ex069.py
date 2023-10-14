"""Exercício 69: Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
A) Quantas pessoas tem mais de 18 anos;
B) Quantos homens foram cadastrados;
C) Quantas mulheres tem menos de 20 anos."""
maior_18 = 0
homem = 0
mulheres_menos_20 = 0
continua = 0
while True:
    idade = int(input('Qual é a sua \033[1;33midade\033[m? '))
    sexo = input('Informe seu \033[1;33msexo\033[m: [F/M] ').lower().strip()
    """if sexo != 'f' and sexo != 'm':
        sexo = input('Informe seu \033[1;33msexo\033[m: [F/M] ').lower().strip()"""
    continua = input('\033[1;33mDeseja continuar\033[m? [S/N] ').lower().strip()
    if continua not in 'sn':
        continua = input('\033[1;33mDeseja continuar\033[m? [S/N] ').lower().strip()
    if idade > 18:
        maior_18 += 1
    if sexo == 'm':
        homem += 1
    if sexo == 'f' and idade < 20:
        mulheres_menos_20 += 1
    if continua != 's':
        break
print('-'*40)
print(f'Fim do programa. Vamos aos resultados:\na) Quantas pessoas tem mais de 18 anos? \033[1;33m{maior_18}\033[m\nb) Quantos homens foram cadastrados? \033[1;33m{homem}\033[m\nc) Quantas mulheres tem menos de 20 anos? \033[1;33m{mulheres_menos_20}\033[m')
print('-'*40)



