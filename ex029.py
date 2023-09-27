#escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada km acima do limite.
velocidade = float(input('Insira a velocidade do carro: '))
if velocidade > 80:
    print('MULTA! Você excedeu o limite permitido de 80km/h. A multa vai custar R${}.'.format((velocidade-80)*7))
print('Tenha um bom dia! Dirija em segurança.')