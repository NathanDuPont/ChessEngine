# ChessEngine Source Code

This section is dedicated to explaining the ChessEngine source code, as well as how to get started with your agentawe. 

The ChessEngine source code has a few primary features, including:
- Allowing the user to create custom Agents with defined reward functions
- Executes games of chess between two defined agents, recording the game state after each move and saving a final video

Information below will be *specific to viewing and modifying the source code*.

## Getting Started

Ensure that the *Getting Started* steps of the `README` in the root have been completed before starting this section.

Open a bash terminal and change directors to the `src` directory. From here, the ChessEngine can be executed, along with any custom agents that you have developed. This can be done by running the following command:

```
python main.py
```

## Creating Custom Agents

Users can create their own agents within the `agents.py` file, located in the `src` directory. There are currently some samples in the file that can be used as reference or starting material. However, if you wish to create your own agent, you need to make sure to follow the below format:

```python
class TODOAgent(BaseAgent):
    """
    Your agent class. Upon final submission, please rename this class to {Team Name}Agent.py, and
    fill in the following:

    Team Name:
    Team Member 1:
    Team Member 2:
    """

    def __init__(self, is_white):
        """
        This method will STAY THE SAME for all agents, but needs to be pasted into each at the beginning
        """
        super().__init__(is_white)

    def heuristic(self, board):
        """
        This method will be DIFFERENT for each agent, and require you to return an integer based on information you pull from the board object.

        :param board: board, Board element containing data about the current game state
        :return: int, Returns the estimated utility of the board state 
        """
```

Your code will go into the `heuristic()` function within the class. In this case, you use the data available to you through the `board` parameter, and use it to return an integer reward. In this case, large positive integers indicate that the model is doing well, large negative integers indicate that the model is doing poorly. More information about the chess board can be found at https://python-chess.readthedocs.io/en/latest/core.html#board.
