# Exercício 97: Faça um programa que tenha a função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.
def escreva(txt):
    print('-'*len(txt))
    print(f'{txt}')
    print('-'*len(txt))

escreva("Testando")
escreva("Olá, mundo!")

