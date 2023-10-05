# 51: Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.
lista_pa = []
primeiro_termo_pa = float(input('Insira o primeiro termo da PA: '))
razão_pa = float(input('Insira a razão da PA: '))
for i in range (10):
    pa = primeiro_termo_pa + (razão_pa * i)
    lista_pa.append(pa)
print(lista_pa)
