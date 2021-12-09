import os
from PIL import Image


class Animator:
    """
    This class is used to animate a game, with a series of images of board states
    """
    def __init__(self, dir):
        self.dir = dir

    def animate(self, queue):
        img_paths = []
        while not queue.empty():
            img_paths.append(Image.open(queue.get()[1]))

        # Combine img_paths into a video
