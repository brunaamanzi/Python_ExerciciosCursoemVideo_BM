"""Desafio 111: Crie um pacote chamado utilidadesCeV que tenha dois módulos internos chamados moeda e dado. Transfira todas as funções utilizadas nos desafios 107, 108 e 109 para o primeiro pacote e mantenha tudo funcionando."""

from ex111.utilidades_CeV import moeda
p = float(input('Insira um número: ').replace(",","."))
moeda.resumo(p,20,12)
moeda.ajuda(moeda.diminuir)