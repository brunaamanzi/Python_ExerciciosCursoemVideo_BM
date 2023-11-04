def leiaDinheiro(num):
        while True:
            num = float(input("Digite o preço: R$"))
            return num
            except ValueError:
                print(f'\033[1;31mERRO! "{num}" é um preço inválido!\033[m')
            if num.isnumeric():
                break
