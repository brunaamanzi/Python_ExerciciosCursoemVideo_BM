# 65: Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
num = 0
lista = []
escolha = 'S'
while escolha == 'S':
    num = int(input('Escolha um número inteiro: '))
    lista.append(num)
    escolha = input('Quer continuar? Selecione SIM ou NÃO [S/N]: ').upper().strip()
lista.sort()
print('A média entre os valores selecionados foi: {:.2f};\nO maior valor selecionado foi: {};\nO menor valor selecionado foi: {}.'.format(sum(lista)/len(lista),lista[-1],lista[0]))
# outra forma sem precisar utilizar o sort, para retornar o maior e menor valor, seria: max(lista),min(lista)