# Exercício 76: Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.
print('='*40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('='*40)
produtos = ('Lápis',1.75,'Borracha',2,'Caderno',15.90,'Estojo',25,'Transferidor',4.20,'Compasso',9.99,'Mochila',120.32,'Canetas',22.30,'Livro',34.90)
for c in range (0,len(produtos)): # não podemos colocar for c in produtos, pois nesse caso tem que ser RANGE
    if c % 2 == 0: # para verificar as posições pares (produtos)
        print(f'{produtos[c]:.<30}',end='')
    else: # para verificar posições ímpares (preços)
        print(f'R${produtos[c]:>8.2f}')
"""print(f'{produtos[0]:.<30}R${produtos[1]:>8}')
print(f'{produtos[2]:.<30}R${produtos[3]:>8}')
print(f'{produtos[4]:.<30}R${produtos[5]:>8}')
print(f'{produtos[6]:.<30}R${produtos[7]:>8}')
print(f'{produtos[8]:.<30}R${produtos[9]:>8}')
print(f'{produtos[10]:.<30}R${produtos[11]:>8}')
print(f'{produtos[12]:.<30}R${produtos[13]:>8}')
print(f'{produtos[14]:.<30}R${produtos[15]:>8}')
print(f'{produtos[16]:.<30}R${produtos[17]:>8}')"""
print('='*40)

