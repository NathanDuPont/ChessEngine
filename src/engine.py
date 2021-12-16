import chess
import chess.engine
import chess.svg
import os
import time
from datetime import datetime
from queue import PriorityQueue
from animation import Animator


class Engine:
    def __init__(self, white_agent, black_agent):
        self.white_agent = white_agent
        self.black_agent = black_agent

    def play(self):
        """
        This function continually plays rounds of the Chess competition until the game is complete.

        Original engine created by Noah Kennedy.
        """
        board = chess.Board()
        count = 0
        time = datetime.now()
        game_identifier = f"{self.white_agent.get_name()}_{self.black_agent.get_name()}_{time.strftime('%d%H%M%S')}"
        dir = f"output/{game_identifier}"
        img_queue = PriorityQueue()

        while not board.is_game_over():
            if count % 2 == 0:
                chosen_move = self.white_agent.make_move(board.copy())
            else:
                chosen_move = self.black_agent.make_move(board.copy())

            board.push(chosen_move)

            s = chess.svg.board(board)

            path = f"{dir}/move{count}.svg"

            os.makedirs(dir, exist_ok=True)

            move_file = open(path, "w")
            move_file.truncate()
            move_file.write(s)
            move_file.close()

            img_queue.put((count, path))

            count += 1

        print(board.outcome().result())

        animator = Animator(dir)
        animator.animate(img_queue)
