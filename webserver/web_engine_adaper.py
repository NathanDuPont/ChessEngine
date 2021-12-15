import chess
import chess.engine
import chess.svg
import os
import time
from datetime import datetime
from queue import PriorityQueue
from animation import Animator


class WebEngine:
    def __init__(self, white_agent, black_agent):
        self.white_agent = white_agent
        self.black_agent = black_agent

        self.board = chess.Board()
        self.count = 0
        self.time = datetime.now()
        game_identifier = f"{self.white_agent.get_name()}_{self.black_agent.get_name()}_{time.strftime('%d%H%M%S')}"
        self.dir = f"output/{game_identifier}"
        self.img_queue = PriorityQueue()
    
    def get_img_location(self):
        return self.dir
    
    def get_player(self, white: bool):
        if white:
            return self.white_agent
        else:
            return self.black_agent

    def next(self):
        """
        This function continually plays rounds of the Chess competition until the game is complete.

        Original engine created by Noah Kennedy.
        """
        def printBoard():
            s = chess.svg.board(self.board)

            path = f"{self.dir}/move{self.count}.svg"

            os.makedirs(self.dir, exist_ok=True)

            move_file = open(path, "w")
            move_file.truncate()
            move_file.write(s)
            move_file.close()

            self.img_queue.put((self.count, path))

        if self.count == 0: #return blank board for the start of the game
            printBoard()
            self.count += 1
            return False


        if not self.board.is_game_over():
            if self.count % 2 == 1:
                chosen_move = self.white_agent.make_move(self.board.copy())
            else:
                chosen_move = self.black_agent.make_move(self.board.copy())
            print(chosen_move)
            print(type(chosen_move))
            self.board.push(chosen_move)

            printBoard()

            self.count += 1

            return False

        else:
            return True
