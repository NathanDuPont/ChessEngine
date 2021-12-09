import chess
# Add in example agents here

"""
Here is one example of an improvement to the basic chess model.

This model takes the position of pieces into account when calculating the min max score
which should make it more intellegent. However, there is deffinately room for improvement.

Also, feel free to copy the tables as they should already be reletively optimized
"""
from extras.position_tables import tables
def heuristic(self, board):
    """
    Determine whose favor the board is in, and by how much.
    Positive values favor white, negative values favor black.

    :param board:
    :return: Returns the estimated utility of the board state.
    """

    def get_piece_utility(self, piece, position):
        """
        Get the utility of a piece.
        :return: Returns the standard chess score for the piece, positive if white, negative if black.
        """
        table_effect = 1 # tables have 1 times the effect, seems to go wonky if this is modified

        piece_symbol = piece.symbol()
        is_white = not piece_symbol.islower()
        index_direction = 1 if is_white else -1

        lower = piece_symbol.lower()
        score = 0

        if lower == 'p':
            score += 10
            score += tables.pawn_table[position * index_direction] * table_effect
        elif lower == 'n':
            score += 30
            score += tables.knight_table[position * index_direction] * table_effect
        elif lower == 'b':
            score += 30
            score += tables.bishop_table[position * index_direction] * table_effect
        elif lower == 'r':
            score += 50
            score += tables.rook_table[position * index_direction] * table_effect
        elif lower == 'q':
            score += 90
            score += tables.queen_table[position * index_direction] * table_effect
        elif lower == 'k':
            score += 900
            score += tables.king_table[position * index_direction] * table_effect
        
        score *= 1 if is_white else -1

        return score


    # Evaluate scores of each piece
    value = sum(
        get_piece_utility(self, board.piece_at(square), square)
        if board.piece_at(square) is not None else 0
        for square in chess.SQUARES
    )


    # If this is a draw, value is 0 (same for both players)
    if board.can_claim_draw():
        value = 0

    return value