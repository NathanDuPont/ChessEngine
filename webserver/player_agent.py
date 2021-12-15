import chess
from chess import Move

class PlayerAgent:

    def __init__(self, is_white):
        """
        Constructor, initialize your fields here.
        :param is_white: Initializes the color of the agent.
        """
        self.is_white = is_white
        self.next_move = ""
    
    def get_name(self):
        return type(self).__name__
    
    def set_next_move(self, move: str):
        self.next_move = move

    def make_move(self, board):
        current_move = Move.from_uci(self.next_move)
        self.next_move = ""
        return current_move
        
    def get_legal_moves(self, board):
        moves = board.legal_moves
        uci_moves = [move.uci() for move in moves]
        return uci_moves