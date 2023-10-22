"""Exercício 105: Faça um programa que tenha uma função notas(), que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:
- Quantidade de notas;
- A maior nota;
- A menor nota;
- A média da turma;
- A situação (opcional)."""
dados = {}
def notas(a,b,c,d,e,sit=False):
    """inserir descrição da função"""
    dados['total']=a
    dados['maior']=b
    dados['menor']=c
    dados['média']=d
    dados['situação']=e
    if dados['média'] >= 7:
        print('Situação: BOA')
        return True
    print(dados)

resp = notas(5.5,9.5,10,6,5,sit=True)
print(resp)