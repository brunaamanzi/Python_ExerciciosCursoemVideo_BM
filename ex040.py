# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
# média abaixo de 5: reprovado
# média entre 5 e 6,9: recuperação
# média 7 ou superior: aprovado
n1 = float(input('Insira a primeira nota: '))
n2 = float(input('Insira a segunda nota: '))
media = (n1 + n2)/2
if media < 5:
    print('Sua média foi {}. Você está \033[1mREPROVADO!\033[m'.format(media))
elif 5 <= media < 7:
    print('Sua média foi {}. Você está na \033[1mRECUPERAÇÃO!\033[m'.format(media))
elif media >= 7:
    print('Sua média foi {}. Você está \033[1mAPROVADO!\033[m'.format(media))

