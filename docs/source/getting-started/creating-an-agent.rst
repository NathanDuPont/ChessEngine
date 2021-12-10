.. This document walks through the basic process of creating your own agent

Creating an Agent
=================

Creating an *Agent* within the provided framework is very easy. We have an interface that needs to be followed to allow for the agent to properly compete; but outside of that, all implementation details are up to you!

Preface
-------

An *Agent* in reinforcement learning is how the computer interacts with the environment. In this case, we are providing code to determine how our own agent learns to play the game, and how it takes actions based on it's current environment. In the end, you are competing to make your agent the best performing out of everyone who is competing.

The BaseAgent Class
-------------------

We have provided an *interface* for you to implement your agent from. In this case, our interface is the `BaseAgent` class, located in `src/base_agent.py`.

In order to follow our interface, you can create a *derived* class in Python in order to inherit all of the functions and attributes of the class.

This can be done by creating your class in the following format:

.. code:: python

    class TODOAgent(BaseAgent):
        # Class code here...

You can change `TODOAgent` to whatever name you want, but need to keep `BaseAgent` as the parent class. This allows for us to put some generally complex logic into the agent, without requiring you to work directly with it.

Creating Your Agent
-------------------

As mentioned above, we require everyone to follow the `BaseAgent` interface. However, you may add or re-implement any of the methods that are provided to you.

For your agent, we recommend starting with one of the examples, or following the template outlined below:

An example implementation you can use is shown below:

.. code:: python

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

With this template, you **do not** need to change the `__init__()` function, and are **only responsible for changing the `heuristic()` function**. 

Implementing a Heuristic
------------------------

Implementing a good heuristic is the primary challenge of this competition. You need to figure out a way to reward your agent for playing Chess correctly against your opponent. This will rely heavily on various Chess tactics, but is very possible even without any Chess experience. 

To implement a heuristic, you will be writing code within the `heuristic()` function in the sample above. This function has two main responsibilities:

1. Take in information about the current state of the game, through the `board` parameter
2. Give the model a reward based on the current state of the game, as an integer. Positive rewards incentivize the model to take the action, negative rewards decentivize the model to take the action.

Information about the `board` parameter can be found on the following website:

https://python-chess.readthedocs.io/en/latest/core.html#board

Specifically, you're looking for the fields on this parameter that tell you about the game.
