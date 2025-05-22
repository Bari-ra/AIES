import math

def minimax(board, depth, is_maximizing_player, game_over_func, evaluate_function, get_available_moves_func, result_func):
    """
    Implements the Minimax algorithm for Tic-Tac-Toe.

    Args:
        board: The current game board state.
        depth: The recursion depth (number of moves remaining).
        is_maximizing_player: True if it's the maximizing player's turn, False otherwise.
        game_over_func: A function that checks if the game is over.
        evaluate_function: A function that evaluates the utility of a board state.
        get_available_moves_func: A function that returns available moves.
        result_func: A function that applies a move to the board.

    Returns:
        The best move for the current player.
    """

    if game_over_func(board):
        return evaluate_function(board)

    if is_maximizing_player:
        best_score = float('-inf')
        for move in get_available_moves_func(board):
            new_board = result_func(board, move)
            score = minimax(new_board, depth + 1, False, game_over_func, evaluate_function, get_available_moves_func, result_func)
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for move in get_available_moves_func(board):
            new_board = result_func(board, move)
            score = minimax(new_board, depth + 1, True, game_over_func, evaluate_function, get_available_moves_func, result_func)
            best_score = min(score, best_score)
        return best_score