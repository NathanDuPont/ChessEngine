def hash_board(board, depth, is_maxing_white):
    """
    Get a representation of the system that we can cache.
    """
    return str(board) + " " + str(depth) + " " + str(is_maxing_white)


def get_piece_utility(piece):
    """
    Get the utility of a piece.
    :return: Returns the standard chess score for the piece, positive if white, negative if black.
    """
    piece_symbol = piece.symbol()
    is_white = not piece_symbol.islower()

    lower = piece_symbol.lower()

    score = 1 if is_white else -1

    if lower == "p":
        score *= 1
    elif lower == "n":
        score *= 3
    elif lower == "b":
        score *= 3
    elif lower == "r":
        score *= 5
    elif lower == "q":
        score *= 9
    elif lower == "k":
        score *= 1_000_000
    return score
