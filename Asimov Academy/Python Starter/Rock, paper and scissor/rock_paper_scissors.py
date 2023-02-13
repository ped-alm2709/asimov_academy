import os
import random

# placar
placar_jogador = 0
placar_computador = 0

# opções
itens = ("Papel", "Pedra", "Tesoura")

while True:
    os.system("cls")
    print("=" * 47)
    print("Bem vindo(a) ao jogo do Pedra, Papel ou Tesoura")
    print("=" * 47)
    print()
    print("PLACAR")
    print("Você: {}".format(placar_jogador))
    print("Computador: {}".format(placar_computador))
    print()
    print("0 – Papel | 1 – Pedra | 2 – Tesoura")
    print()
    j = int(input("Qual a sua jogada? "))
    pc = random.randint(0, 2)
    print()
    print("Sua jogada: {}".format(itens[j]))
    print("Jogada do computador: {}".format(itens[pc]))
    print()

    if j == pc:
        print("Empate. Ninguém pontua")
    elif (j == 0 and pc == 2) or (j == 1 and pc == 0) or (j == 2 and pc == 1):
        print("O computador vence")
        placar_computador = placar_computador + 1
    else:
        print("O jogador vence")
        placar_jogador = placar_jogador + 1

    print()
    print("=" * 35)
    print("Jogar novamente? 0 – SIM | 1 – NÃO")
    if int(input()) == 1:
        break
