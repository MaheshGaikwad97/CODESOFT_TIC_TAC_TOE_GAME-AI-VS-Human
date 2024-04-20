import random

def display_board(board):
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")

def check_win(board, player):
    # Check rows
    for i in range(0, 9, 3):
        if board[i] == board[i+1] == board[i+2] == player:
            return True
    # Check columns
    for i in range(3):
        if board[i] == board[i+3] == board[i+6] == player:
            return True
    # Check diagonals
    if board[0] == board[4] == board[8] == player:
        return True
    if board[2] == board[4] == board[6] == player:
        return True
    return False

def check_tie(board):
    return ' ' not in board

def get_human_move(board):
    while True:
        move = input("Enter your move (1-9): ")
        if move.isdigit() and 1 <= int(move) <= 9 and board[int(move)-1] == ' ':
            return int(move) - 1
        print("Invalid move. Try again.")

def get_ai_move(board):
    # Check if the AI can win
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            if check_win(board, 'O'):
                return i
            board[i] = ' '

    # Check if the human can win
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'X'
            if check_win(board, 'X'):
                board[i] = 'O'
                return i
            board[i] = ' '

    # If no winning move, make a random move
    moves = [i for i in range(9) if board[i] == ' ']
    return random.choice(moves)

def play_game():
    board = [' '] * 9
    current_player = 'X'

    while True:
        display_board(board)
        if current_player == 'X':
            move = get_human_move(board)
            board[move] = 'X'
        else:
            move = get_ai_move(board)
            board[move] = 'O'
            print(f"AI moved to position {move+1}.")

        if check_win(board, current_player):
            display_board(board)
            if current_player == 'X':
                print("You win!")
            else:
                print("AI wins!")
            return

        if check_tie(board):
            display_board(board)
            print("It's a tie!")
            return

        if current_player == 'X':
            current_player = 'O'
        else:
            current_player = 'X'

play_game()
