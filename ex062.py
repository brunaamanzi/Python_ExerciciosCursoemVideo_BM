# refaça o desafio 61, perguntando para o usuário se ele quer ler mais algum termo. só encerra quando a resposta for 0

primeiro_termo = int(input('Insira o 1º termo da PA: '))
razao = int(input('Insira a razão da PA: '))
decimo_termo = primeiro_termo + (10 - 1) * razao
pa = []
pa.append(primeiro_termo)
while decimo_termo not in pa:
    primeiro_termo += razao
    pa.append(primeiro_termo)
print(pa)
opção = int(input('Você deseja ler mais alguns termos da PA? Quantos? Digite 0 para encerrar. '))
termo_opção = primeiro_termo + opção  * razao
while opção > 0 and termo_opção not in pa:
    primeiro_termo += razao
    pa.append(primeiro_termo)
    print(pa)


