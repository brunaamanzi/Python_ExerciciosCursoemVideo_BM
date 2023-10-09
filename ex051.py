# 51: Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.
"""lista_pa = []
primeiro_termo_pa = float(input('Insira o primeiro termo da PA: '))
razão_pa = float(input('Insira a razão da PA: '))
for i in range (10):
    pa = primeiro_termo_pa + (razão_pa * i)
    lista_pa.append(pa)
print(lista_pa)"""
primeiro_termo = int(input('Escreva aqui o 1º termo da PA: '))
razao = int(input('Agora informe a razão da PA: '))
decimo_termo = primeiro_termo + (10 - 1) * razao
for c in range (primeiro_termo,decimo_termo+1,razao):
    print(c,end=' -> ')
print('ACABOU')