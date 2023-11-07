from ex115.lib.interface import * # para importar tudo: *
from ex115.lib.arquivo import *
from time import sleep

arq = 'cursoemvideo.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['Ver Pessoas Cadastradas','Cadastrar Nova Pessoa','Sair do Programa'])
    if resposta == 1:
        # Opção de listar conteúdo de um arquivo:
        lerArquivo(arq)
    elif resposta == 2:
        #Opção de cadastrar uma nova pessoa
        cabeçalho('NOVO CADASTRO')
        nome = input('Nome: ')
        idade = leiaInt('Idade: ')
        cadastrar(arq,nome,idade)
    elif resposta == 3:
        # Opção de sair do programa
        cabeçalho('Saindo do Programa... Até logo!')
        break
    else:
        #digitou opção errada no MENU
        print('\033[1;31mERRO! Digite uma opção válida.\033[m')
    sleep(1)
