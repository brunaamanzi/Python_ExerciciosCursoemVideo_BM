"""Exercício 105: Faça um programa que tenha uma função notas(), que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:
- Quantidade de notas;
- A maior nota;
- A menor nota;
- A média da turma;
- A situação (opcional)."""
def notas(*n,sit=False):
    """Função para analisar notas e situações de vários alunos.
    :param n: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma.
    """
    dados = {}
    dados['qtde']=len(n)
    dados['maior']=max(n)
    dados['menor']=min(n)
    dados['média']=sum(n)/len(n)
    if sit:
        if dados['média'] >= 7:
            dados['situação']='APROVADO'
        elif dados['média'] >= 5:
            dados['situação']='EM RECUPERAÇÃO'
        else:
            dados['situação']='REPROVADO'
    return dados

resp = notas(5.5,2)
print(resp)