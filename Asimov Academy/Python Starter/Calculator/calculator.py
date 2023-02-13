import os


def escolhe_operacao():
    print("0: Soma (+)")
    print("1: Subtração (-)")
    print("2: Multiplicação (*)")
    print("3: Divisão (/)")
    print("4: Exponenciação (**)\n")

    operador = int(input("Digite o da operação que deseja realizar.\n"))

    if operador == 0:
        print("Operação escolhida: Soma (+)")
        n1 = int(input("Qual o primeiro da operação?\n"))
        n2 = int(input("Qual o segundo da operação?\n"))
        print("{} + {} = {}\n".format(n1, n2, (n1 + n2)))
        print("Deseja realizar outra operação?")
        resetar = int(input("1: Sim\n2: Não\n"))

        if resetar == 1:
            if os.name == "nt":
                os.system("cls")
            else:
                os.system("clear")
            escolhe_operacao()
        elif resetar == 2:
            print("Obrigado por utilizar a calculadora Python do Pedro!")
    elif operador == 1:
        print("Operação escolhida: Subtração (-)")
        n1 = int(input("Qual o primeiro da operação?\n"))
        n2 = int(input("Qual o segundo da operação?\n"))
        print("{} - {} = {}\n".format(n1, n2, (n1 - n2)))
        print("Deseja realizar outra operação?")
        resetar = int(input("1: Sim\n2: Não\n"))

        if resetar == 1:
            if os.name == "nt":
                os.system("cls")
            else:
                os.system("clear")
            escolhe_operacao()
        elif resetar == 2:
            print("Obrigado por utilizar a calculadora Python do Pedro!")
    elif operador == 2:
        print("Operação escolhida: Multiplicação (*)")
        n1 = int(input("Qual o primeiro da operação?\n"))
        n2 = int(input("Qual o segundo da operação?\n"))
        print("{} x {} = {}\n".format(n1, n2, (n1 * n2)))
        print("Deseja realizar outra operação?")
        resetar = int(input("1: Sim\n2: Não\n"))

        if resetar == 1:
            if os.name == "nt":
                os.system("cls")
            else:
                os.system("clear")
            escolhe_operacao()
        elif resetar == 2:
            print("Obrigado por utilizar a calculadora Python do Pedro!")
    elif operador == 3:
        print("Operação escolhida: Divisão (/)")
        n1 = float(input("Qual o primeiro da operação?\n"))
        n2 = float(input("Qual o segundo da operação?\n"))
        print("{} / {} = {:.2f}\n".format(n1, n2, (n1 / n2)))
        print("Deseja realizar outra operação?")
        resetar = int(input("1: Sim\n2: Não\n"))

        if resetar == 1:
            if os.name == "nt":
                os.system("cls")
            else:
                os.system("clear")
            escolhe_operacao()
        elif resetar == 2:
            print("Obrigado por utilizar a calculadora Python do Pedro!")
    elif operador == 4:
        print("Operação escolhida: Exponenciação (**)")
        n1 = float(input("Qual será o exponenciando da operação?\n"))
        n2 = float(input("Qual o exponenciador da operação?\n"))
        print("{} elevado a {} = {:.2f}\n".format(n1, n2, (n1 ** n2)))
        print("Deseja realizar outra operação?")
        resetar = int(input("1: Sim\n2: Não\n"))

        if resetar == 1:
            if os.name == "nt":
                os.system("cls")
            else:
                os.system("clear")
            escolhe_operacao()
        elif resetar == 2:
            print("Obrigado por utilizar a calculadora Python do Pedro!")
    else:
        print('Opção não válida, digite novamente: ')
        escolhe_operacao()


escolhe_operacao()
