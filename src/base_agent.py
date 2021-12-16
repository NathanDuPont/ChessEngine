import chess
from util import hash_board, get_piece_utility


class BaseAgent:
    """
    The base agent class. This supports the basic logic required to use the agent framework in competition,
    requiring the heuristic to be re-implemented in a derived/child class (for simplicity). For those with
    more experience, the BaseAgent class does NOT need to be used, as long as the following interface is followed.

    Original base agent created by Noah Kennedy.
    """

    depth = 3
    cache = {}

    def __init__(self, is_white):
        """
        Constructor, initialize your fields here.
        :param is_white: Initializes the color of the agent.
        """
        self.is_white = is_white

    def get_name(self):
        """
        Report the agent name.
        """
        return type(self).__name__

    def heuristic(self, board):
        """
        Determine whose favor the board is in, and by how much.
        Positive values favor white, negative values favor black.

        This class is overwritten by a user's implemented agent
        :param board:
        :return: Returns the estimated utility of the board state.
        """
        raise NotImplementedError

    def make_move(self, board):
        """
        Determine the next move to make, given the current board.
        :param board: The chess board
        :return: The selected move
        """
        global_score = -1e8 if self.is_white else 1e8
        chosen_move = None

        for move in board.legal_moves:
            board.push(move)

            local_score = self.minimax(
                board, self.depth - 1, not self.is_white, -1e8, 1e8
            )

            self.cache[
                hash_board(board, self.depth - 1, not self.is_white)
            ] = local_score

            if self.is_white and local_score >= global_score:
                global_score = local_score
                chosen_move = move
            elif not self.is_white and local_score <= global_score:
                global_score = local_score
                chosen_move = move

            board.pop()

        return chosen_move

    def minimax(self, board, depth, is_maxing_white, alpha, beta):
        """
        Minimax implementation with alpha-beta pruning.
        Source: https://github.com/devinalvaro/yachess
        :param board: Chess board
        :param depth: Remaining search depth
        :param is_maxing_white: Whose score are we maxing?
        :param alpha: Alpha-beta pruning value
        :param beta: Alpha-beta pruning value
        :return: The utility of the board state
        """
        # Check if board state is in cache
        if hash_board(board, depth, is_maxing_white) in self.cache:
            return self.cache[hash_board(board, depth, is_maxing_white)]

        # Check if game is over or we have reached maximum search depth.
        if depth == 0 or not board.legal_moves:
            self.cache[hash_board(board, depth, is_maxing_white)] = self.heuristic(
                board
            )
            return self.cache[hash_board(board, depth, is_maxing_white)]

        # General case
        best_score = -1e8 if is_maxing_white else 1e8
        for move in board.legal_moves:
            board.push(move)

            local_score = self.minimax(
                board, depth - 1, not is_maxing_white, alpha, beta
            )
            self.cache[hash_board(board, depth - 1, not is_maxing_white)] = local_score

            if is_maxing_white:
                best_score = max(best_score, local_score)
                alpha = max(alpha, best_score)
            else:
                best_score = min(best_score, local_score)
                beta = min(beta, best_score)

            board.pop()

            if beta <= alpha:
                break

        self.cache[hash_board(board, depth, is_maxing_white)] = best_score

        return self.cache[hash_board(board, depth, is_maxing_white)]
