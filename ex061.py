# 61: Refaça o desafio 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão utilizando a estrutura while.
primeiro_termo = int(input('Insira o 1º termo de uma PA: '))
razao = int(input('Insira a razão da PA: '))
pa = []
pa.append(primeiro_termo)
decimo_termo = primeiro_termo + (10 - 1) * razao
while decimo_termo not in pa:
    primeiro_termo += razao
    pa.append(primeiro_termo)
print(pa)

