.. This document outlines how to test an agent within the program

Testing an Agent
================

Once you get your agent completed, it's time to test it. This will be done within the `main.py` file, located within the `src/` directory. 

The code within the `main.py` file follows the format below:

.. code:: python

    if __name__ == "__main__":
        white_agent = CustomAgent(True)
        black_agent = CustomAgent(False)
        engine = Engine(white_agent, black_agent)

        engine.play()

In this case, one of the agents will be set to `white_agent`, and the other to `black_agent`. If you want to test your agent, replace one of the two to your Agent class, and run the file.

For example, if your agent is called `TODOAgent`, your code will look like the following:

.. code:: python

    if __name__ == "__main__":
        white_agent = TODOAgent(True)
        black_agent = CustomAgent(False)
        engine = Engine(white_agent, black_agent)

        engine.play()

To test the code, you can open a terminal within the `src/` directory and run the following:

.. code:: bash

    python main.py

Viewing Model Results
---------------------

Model results can be viewed within the `src/output/` directory, under a separate folder. The game information is saved under a new folder during every run, following the pattern `{white_agent}_{black_agent}_{Unique ID}`.

There will be a video of the full game saved to the folder, along with images of the game board after each step.