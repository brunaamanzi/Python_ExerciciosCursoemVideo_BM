from ex115.lib.interface import * # para importar tudo: *
from time import sleep
cabeçalho('testando 1 2 3')
while True:
    resposta = menu(['Ver Pessoas Cadastradas','Cadastrar Nova Pessoa','Sair do Programa'])
    if resposta == 1:
        cabeçalho('Opção 1')
    elif resposta == 2:
        cabeçalho('Opção 2')
    elif resposta == 3:
        cabeçalho('Saindo do Programa... Até logo!')
    else:
        print('\033[1;31mERRO! Digite uma opção válida.\033[m')
    sleep(1)
