import chess
from base_agent import BaseAgent
from util import get_piece_utility, hash_board


class CustomAgent(BaseAgent):
    """
    Your agent class. Upon final submission, please rename this class to {Team Name}Agent.py, and
    fill in the following:

    Team Name:
    Team Member 1:
    Team Member 2:
    """

    def __init__(self, is_white):
        super().__init__(is_white)

    def heuristic(self, board):
        """
        Determine whose favor the board is in, and by how much.
        Positive values favor white, negative values favor black.

        This example bases the heuristic on the total number of pieces
        for each player. A positive number indicates that the player with
        white pieces is in favor, a negative number indicates that the
        player with black pieces is in favor. In this example, the model
        will learn to optimize it's gameplay in order to make the score
        as positive or negative as possible, coordinating to it's color.

        :param board:
        :return: Returns the estimated utility of the board state.
        """
        # Evaluate scores of each piece
        value = sum(
            get_piece_utility(board.piece_at(square))
            if board.piece_at(square) is not None
            else 0
            for square in chess.SQUARES
        )

        # If this is a draw, value is 0 (same for both players)
        if board.can_claim_draw():
            value = 0

        return value
