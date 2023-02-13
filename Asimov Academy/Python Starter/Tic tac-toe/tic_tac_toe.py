import os
import random
import time


board = []


def clean_screen():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def display_board():
    global board
    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                print(" _ ", end=' ')
            elif board[i][j] == 1:
                print(" X ", end=' ')
            elif board[i][j] == -1:
                print(" O ", end=' ')

        print()


def menu():
    global board
    continue_game = 1
    board = [[0 for i in range(3)] for j in range(3)]
    while continue_game:
        print('=========')
        print('Bem vindo ao Jogo da Velha:')
        print('=========\n')
        print('Você será o "X" e o computador o "O".')
        display_board()
        move_calculate()
        print('\nDeseja jogar novamente?\n')
        play_again = int(input('0 - Não | 1 - Sim\n'))
        if play_again == 1:
            clean_screen()
            print('Bora pra outra partida!\n')
            board = [[0 for i in range(3)] for j in range(3)]
            display_board()
            move_calculate()
        elif play_again == 0:
            clean_screen()
            continue_game = 0
            print('Até a próxima, campeão!')
            time.sleep(3)
            quit()
        else:
            print('Valor inserido não corresponde a uma opção válida..')
            print('Saindo...')
            time.sleep(3)
            quit()


def move_calculate():
    global board
    while calculate_winner() == 0:
        print('\nSua vez de jogar: ')
        y_col = int(input(
            '\nEscolha uma COLUNA: 1 - 2 - 3\n'
        ))
        y_row = int(input(
            'Escolha uma LINHA: 1 - 2 - 3\n'
        ))
        if y_col not in list(range(1, 4)) or y_row not in list(range(1, 4)):
            print('\nColuna e/ou linha selecionada não existe(m)!')
            print('Vamos tentar novamente:\n')
            calculate_winner()
        else:
            if board[y_row - 1][y_col - 1] == 1:
                print('Ops, não dá pra escolher um campo já marcado!')
                print('Vamos tentar novamente:\n')
                calculate_winner()
            elif board[y_row - 1][y_col - 1] == -1:
                print('Ops, não dá pra escolher um campo já marcado!')
                print('Vamos tentar novamente:\n')
                calculate_winner()
            elif board[y_row - 1][y_col - 1] == 0:
                board[y_row - 1][y_col - 1] = 1
                computer_move()
                display_board()
                calculate_winner()
    if calculate_winner() == 3:
        clean_screen()
        print('Parabéns campeão, você ganhou!')
    elif calculate_winner() == -3:
        clean_screen()
        print('Eis que a máquina supera o homem!')


def computer_move():
    pc_row = random.randint(0, 2)
    pc_col = random.randint(0, 2)
    if board[pc_row][pc_col] == -1 or board[pc_row][pc_col] == 1:
        pc_row = random.randint(0, 2)
        pc_col = random.randint(0, 2)
    elif board[pc_row][pc_col] == 0:
        board[pc_row][pc_col] = -1


def calculate_winner():
    # checando linhas
    for i in range(3):
        result = board[i][0] + board[i][1] + board[i][2]
        if result == 3 or result == -3:
            return result

    # checando colunas
    for i in range(3):
        result = board[0][i] + board[1][i] + board[2][i]
        if result == 3 or result == -3:
            return result

    # checando diagonais
    diagonal1 = board[0][0] + board[1][1] + board[2][2]
    diagonal2 = board[0][2] + board[1][1] + board[2][0]
    if diagonal1 == 3 or diagonal2 == 3:
        return 3
    elif diagonal1 == -3 or diagonal2 == -3:
        return -3

    return 0


menu()
