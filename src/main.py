from agents import *
from engine import Engine

import imageio
import os

if __name__ == "__main__":
    white_agent = CustomAgent(True)
    black_agent = CustomAgent(False)
    engine = Engine(white_agent, black_agent)

    engine.play()
