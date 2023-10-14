# refaça o desafio 61, perguntando para o usuário se ele quer ler mais algum termo. só encerra quando a resposta for 0

primeiro_termo = int(input('\033[1;31mInsira o 1º termo de uma PA: '))
razao = int(input('Insira a razão da PA: \033[m'))
termo = primeiro_termo
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print('{}'.format(termo),end=' -> ')
        termo += razao
        cont += 1
    print('PAUSA')
    mais = int(input('\033[1;31mQuantos termos a mais você deseja mostrar? \033[m'))
print('\033[1;41mO programa foi finalizado com {} termos mostrados.\033[m'.format(total))