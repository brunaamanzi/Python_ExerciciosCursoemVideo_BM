numero = input("Digite um número de até quatro dígitos: ")

if len(numero) > 4:
    print("Número fora do intervalo permitido.")
else:
    # Preencher com zeros à esquerda para garantir 4 dígitos
    numero = numero.zfill(4)

    # Mostrar os resultados
    print(f"Milhar: {numero[0]}")
    print(f"Centena: {numero[1]}")
    print(f"Dezena: {numero[2]}")
    print(f"Unidade: {numero[3]}")