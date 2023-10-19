# Exercício 90: Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.
# Considerando média 7 aprovada e abaixo disso reprovada:
dados = dict()
dados['nome']=input('Nome: ')
dados['média']=float(input(f'Média de {dados["nome"]}: '))
print(f'Nome é igual a {dados["nome"]}')
print(f'Média é igual a {dados["média"]}')
print('Situação é igual a Aprovado' if dados["média"] >= 7 else 'Situação é igual a Reprovado')