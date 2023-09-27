# Desenvolva uma lógica que leia o peso e a altura de uma pessoa. Calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
# Abaixo de 18.5: abaixo do peso
# De 18.5 até 24.99: peso ideal
# De 25 até 29.99: sobrepeso
# 30 até 40: obesidade
# acima de 40: obesidade mórbida
print('-'*42)
print('\033[1;35;40mOlá! Vamos calcular e analisar o seu IMC?\033[m')
print('-'*42)
peso = float(input('Insira seu peso em KG: '))
altura = float(input('Insira sua altura em metros: '))
IMC = peso / (altura**2)
print('O seu IMC é: {:.2f}'.format(IMC))
if IMC < 18.5:
    print('Você está \033[1mabaixo do peso!\033[m')
elif 18.5 <= IMC < 25:
    print('Você está no \033[1mpeso ideal!\033[m')
elif 25 <= IMC < 30:
    print('Você está com \033[1msobrepeso!\033[m')
elif 30 <= IMC < 40:
    print('Você está com \033[1mobesidade!\033[m')
elif IMC > 40:
    print('Você está com \033[1mobesidade mórbida!\033[m')
