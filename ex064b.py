print('Olá! Bem vindo ao nosso Somatório.\nInsira quantos números você quiser e iremos realizar a soma entre eles. Para encerrar, digite 999.')
cont = soma = num = 0
num = int(input("Insira um número: "))
while num != 999:
    soma += num
    cont += 1
    num = int(input("Insira um número: "))
print('Você escreveu {} números e a soma entre eles é {}.'.format(cont,soma))
