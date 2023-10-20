# Exercício 90: Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.
# Considerando média 7 aprovada e abaixo disso reprovada:
dados = dict()
dados['nome']=input('Nome: ')
dados['média']=float(input(f'Média de {dados["nome"]}: '))
if dados["média"] >= 7:
    dados['situação']='Aprovado'
elif 7 > dados["média"] > 5:
    dados['situação']='Recuperação'
else:
    dados['situação']='Reprovado'
for k,v in dados.items():
    print(f' - {k} é igual a {v}.')
