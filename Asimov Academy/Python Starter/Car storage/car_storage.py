import os

carros = [
    ("Chevrolet Tracker", 120),
    ("Chevrolet Onix", 90),
    ("Chevrolet Spin", 150),
    ("Hyundai HB20", 85),
    ("Hyundai Tucson", 120),
    ("Fiat Uno", 60),
    ("Fiat Mobi", 70),
    ("Fiat Pulse", 130),
]
alugados = []


def clean_screen():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def mostrar_lista_de_carros(lista_de_carros):
    # O loop criará uma lista com os índicies (i) das tuplas (car)
    for i, car in enumerate(lista_de_carros):
        print("[{}] {} - R$ {} /dia.".format(i, car[0], car[1]))


while True:
    clean_screen()
    print("=========")
    print("Bem vindo à locadora de carros!")
    print("=========")
    print("O que deseja fazer?")
    print(
        "0 - Mostrar portifólio | 1 - Alugar um carro | 2 - Devolver um carro"
        )
    op = int(input())

    clean_screen()
    if op == 0:
        mostrar_lista_de_carros(carros)

    elif op == 1:
        mostrar_lista_de_carros(carros)
        print("==========")
        print("Escolha o código do carro:")
        cod_car = int(input())
        print("Por quantos dias você deseja alugar este carro?")
        dias = int(input())
        clean_screen()

        print("Você escolheu {} por {} dias.".format(carros[cod_car][0], dias))
        print("O aluguel totalizaria R$ {}.".format(dias * carros[cod_car][1]))
        print("Deseja alugar?")
        print("0 - SIM | 1 - NÃO")
        conf = int(input())
        if conf == 0:
            print("{} alugado por {} dias.".format(carros[cod_car][0], dias))
            alugados.append(carros.pop(cod_car))

    elif op == 2:
        if len(alugados) == 0:
            print("Não há carros para devolver.")
        else:
            print("Lista de carros alugados. Qual você deseja devolver?")
            mostrar_lista_de_carros(alugados)
            print("")
            print("Escolha o código do carro que deseja devolver:")
            cod = int(input())
            if conf == 0:
                print("Obrigado por devolver o {}".format(alugados[cod][0]))
                carros.append(alugados.pop(cod))

    print("")
    print("===========")
    print("0 para CONTINUAR | 1 para SAIR")
    if float(input()) == 1:
        break
