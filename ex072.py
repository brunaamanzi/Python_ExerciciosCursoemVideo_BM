# Exercício 72: Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até 20. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
tupla = ('zero','um','dois','três','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','quatorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte')
numero = int(input('Escolha um número entre 0 e 20: '))
print(f'O número escolhido foi {tupla[numero]}')
