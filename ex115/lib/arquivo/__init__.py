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