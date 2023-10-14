print('61: Refaça o desafio 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão utilizando a estrutura while.')
primeiro_termo = int(input('Insira o 1º termo de uma PA: '))
razao = int(input('Insira a razão da PA: '))
termo = primeiro_termo
cont = 1
while cont <= 10:
    print('{}'.format(primeiro_termo),end=' -> ')
    primeiro_termo += razao
    cont += 1
print('FIM')
