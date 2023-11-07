from ex115.lib.interface import *

def arquivoExiste(nome):
    try:
        a = open(nome,'rt') # rt: read text
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def criarArquivo(nome):
    try:
        a = open(nome,'wt+') # write text + (se não existir, cria)
        a.close()
    except:
        print('Houve um erro na criação do arquivo!')
    else:
        print(f'Arquivo {nome} criado com sucesso!')

def lerArquivo(nome):
    try:
        a = open(nome,'rt')
    except:
        print('Erro ao ler o arquivo!')
    else:
        cabeçalho('PESSOAS CADASTRADAS')
        for linha in a:
            dado = linha.split(';') #para dividir dados de listas
            dado[1]=dado[1].replace('\n','')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
    finally:
        a.close()

def cadastrar(arq,n='desconhecido',i = 0):
    try:
        a = open(arq,'at') #append text
    except:
        print('Houve um erro na abertura do arquivo.')
    else:
        try:
            a.write(f'{n};{i}\n')
        except:
            print('Houve um erro na hora de escrever os dados.')
        else:
            print(f'Novo registro de {n} adicionado.')
            a.close()