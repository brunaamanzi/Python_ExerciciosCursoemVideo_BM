# Exercício 96: Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área de terreno.
def tit():
    print(f'{"Controle de Terrenos":^30}')
    print('-'*30)
def terreno(larg,comp):
    area = larg * comp
    print(f'A área do terreno {larg:.1f}x{comp:.1f} é de {area:.1f}m².')
tit()
larg = float(input('LARGURA (m): '))
comp = float(input('COMPRIMENTO (m): '))
terreno(larg,comp)