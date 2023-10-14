# refaça o desafio 61, perguntando para o usuário se ele quer ler mais algum termo. só encerra quando a resposta for 0

primeiro_termo = int(input('\033[1;32mInsira o 1º termo de uma PA: '))
razao = int(input('Insira a razão da PA: \033[m'))
termo = primeiro_termo
cont = 1
while cont <= 10:
    print('{}'.format(primeiro_termo),end=' -> ')
    primeiro_termo += razao
    cont += 1
print('PAUSA')
opção = 1
while opção != 0:
    opção = int(input('\033[1;32mDeseja ver mais quantos termos? Digite 0 para encerrar. \033[m'))
    cont = 1
    while cont <= opção:
        print('{}'.format(primeiro_termo),end=' -> ')
        primeiro_termo += razao
        cont += 1
    print('PAUSA' if opção > 0 else 'FIM')


