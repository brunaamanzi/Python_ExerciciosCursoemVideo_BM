#Desafio 10: Crie um programa que leia quanto dinheiro a pessoa tem na carteira e mostre quantos dólares ela poderia comprar. Considera US$1,00 = R$3,27.
dolar=float(3.27)
carteira=float(input('Qual valor você tem em sua carteira? '))
print('Com R${} você pode comprar US${:.2f}'.format(carteira,carteira/dolar))