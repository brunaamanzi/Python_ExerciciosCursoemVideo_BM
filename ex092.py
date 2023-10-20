# Exercício 92: Crie um programa que leia: nome, ano de nascimento e carteira de trabalho, e cadastre-os (com idade) em um dicionário. Se por acaso a CTPS for diferente de zero, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
# Considera que para se aposentar, é necessário ter 35 anos de contribuição.
dados = dict()
dados['nome']=input('Nome: ')
ano_nascimento = int(input('Ano de Nascimento: '))
from datetime import date
ano_atual = date.today().year
dados['idade']=ano_atual-ano_nascimento
dados['ctps']=int(input('Carteira de Trabalho (0 não tem): '))
if dados['ctps'] != 0:
    dados['contratação']=int(input('Ano de contratação: '))
    dados['salário']=float(input('Salário: R$ '))
    dados['aposentadoria']=ano_atual-dados['contratação']
print(dados)
for k,v in dados.items():
    print(f'{k} tem o valor {v}')