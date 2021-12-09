.. This document outlines how to get the repository set up locally

Repository Setup
================

With Git and Python installed, we can now properly get the repository set up.

Open up your web browser and go to https://github.com/NathanDuPont/ChessEngine. This is the GitHub repository that contains all of the code required to start the project.

Obtaining the Code
------------------

Obtaining the code can be done one of two ways. For those who are unfamiliar with Git, we recommend **downloading the code**. For those who are familiar with Git, we recommend **cloning the repository**.

**Downloading the Code**

Click below to obtain the code:

`Download the ChessEngine Repository`_

.. _Download the ChessEngine Repository: https://github.com/NathanDuPont/ChessEngine/archive/refs/heads/main.zip

**Cloning the Repository**

Open up Git Bash in the folder you wish to start your project in. From there, run one of the following commands:

*If you have SSH keys set up*:

.. code:: bash

    git clone git@github.com:NathanDuPont/ChessEngine.git


*If you do not have SSH keys set up*:

.. code:: bash

    https://github.com/NathanDuPont/ChessEngine.git


Installing Required Packages
----------------------------

.. note::

    This section is ideally performed within a Conda environment or Python Virtual Environment (venv), but can be done without them. This guide will walk through the setup process without using an environment.

With the code downloaded, open it in an IDE of your choice. From there, open up Git Bash (or another terminal) within the **root project folder**. Run the following commands within your terminal:

.. code:: bash

    pip install -r requirements.txt

This will install all of the required packages to run the Chess program. With this installed, you can move onto the next section of the guide.