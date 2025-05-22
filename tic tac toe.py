import math
import time
import copy

# Constants
PLAYER = 'X'
AI = 'O'
EMPTY = ' '

# Initialize board
def create_board():
    return [[EMPTY for _ in range(3)] for _ in range(3)]

# Print the board
def print_board(board):
    for row in board:
        print('|'.join(row))
        print('-' * 5)

# Check for winner
def check_winner(board, player):
    for row in board:
        if all([cell == player for cell in row]):
            return True
    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True
    if all([board[i][i] == player for i in range(3)]) or all([board[i][2-i] == player for i in range(3)]):
        return True
    return False

# Check for draw
def is_draw(board):
    return all(cell != EMPTY for row in board for cell in row)

# Get available moves
def get_available_moves(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == EMPTY]

# Evaluate board
def evaluate(board):
    if check_winner(board, AI):
        return 1
    elif check_winner(board, PLAYER):
        return -1
    else:
        return 0

# Minimax Algorithm
def minimax(board, is_maximizing):
    if check_winner(board, AI) or check_winner(board, PLAYER) or is_draw(board):
        return evaluate(board)

    if is_maximizing:
        best_score = -math.inf
        for (i, j) in get_available_moves(board):
            board[i][j] = AI
            score = minimax(board, False)
            board[i][j] = EMPTY
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for (i, j) in get_available_moves(board):
            board[i][j] = PLAYER
            score = minimax(board, True)
            board[i][j] = EMPTY
            best_score = min(score, best_score)
        return best_score

# Minimax with Alpha-Beta Pruning
def minimax_ab(board, is_maximizing, alpha, beta):
    if check_winner(board, AI) or check_winner(board, PLAYER) or is_draw(board):
        return evaluate(board)

    if is_maximizing:
        best_score = -math.inf
        for (i, j) in get_available_moves(board):
            board[i][j] = AI
            score = minimax_ab(board, False, alpha, beta)
            board[i][j] = EMPTY
            best_score = max(score, best_score)
            alpha = max(alpha, score)
            if beta <= alpha:
                break
        return best_score
    else:
        best_score = math.inf
        for (i, j) in get_available_moves(board):
            board[i][j] = PLAYER
            score = minimax_ab(board, True, alpha, beta)
            board[i][j] = EMPTY
            best_score = min(score, best_score)
            beta = min(beta, score)
            if beta <= alpha:
                break
        return best_score

# AI move using Minimax
def best_move_minimax(board):
    best_score = -math.inf
    move = None
    for (i, j) in get_available_moves(board):
        board[i][j] = AI
        score = minimax(board, False)
        board[i][j] = EMPTY
        if score > best_score:
            best_score = score
            move = (i, j)
    return move

# AI move using Alpha-Beta Pruning
def best_move_ab(board):
    best_score = -math.inf
    move = None
    for (i, j) in get_available_moves(board):
        board[i][j] = AI
        score = minimax_ab(board, False, -math.inf, math.inf)
        board[i][j] = EMPTY
        if score > best_score:
            best_score = score
            move = (i, j)
    return move

# Compare performance
def compare_performance():
    board = create_board()
    board[0][0] = PLAYER
    board[1][1] = AI
    board[0][1] = PLAYER

    print("Initial Board:")
    print_board(board)

    board1 = copy.deepcopy(board)
    start = time.time()
    move1 = best_move_minimax(board1)
    end = time.time()
    print("\nMinimax chose move:", move1)
    print("Time taken (Minimax):", round(end - start, 6), "seconds")

    board2 = copy.deepcopy(board)
    start = time.time()
    move2 = best_move_ab(board2)
    end = time.time()
    print("\nAlpha-Beta Pruning chose move:", move2)
    print("Time taken (Alpha-Beta):", round(end - start, 6), "seconds")

# Run performance comparison
if __name__ == "__main__":
    compare_performance()

