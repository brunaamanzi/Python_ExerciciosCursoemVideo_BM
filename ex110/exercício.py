"""Desafio 109: Adicione o módulo moeda.py criado nos desafios anteriores, uma função chamada resumo(), que mostre na tela algumas informações geradas pelas funções que já temos no módulo criado até aqui."""

from ex110 import moeda

# moeda.ajuda(moeda)
valor = float(input('Digite o preço: R$'))
moeda.resumo(valor,2,3)