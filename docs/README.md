# ChessEngine Documentation

**Documentation Website**: TODO

This section is dedicated to explaining the ChessEngine documentation website, as well as outline how to contribute to the documentation. 

This website was created to outline how to use the Chess engine, and outline the features available within the source code. This documentation is a living document, and allows expansion to help capture the use cases of the code in this repository.

Information below will be *specific to viewing and modifying the documentation*.

## Getting Started

To get this functioning locally, there are a few prerequisitves that you will need to have installed.

- Git
- Python (3.x.x)
- Pip
- SSH configured with your GitHub account

Once these are met, installation of the repository can continue.

First, run the following command in the directory you wish to save the project folder to:

```
git@github.com:NathanDuPont/ChessEngine.git
```

From here, open up the project in an IDE such as *Visual Studio Code*. **For the following steps, it would be ideal to run them within a Python Virtual Environment, or venv**.

Open a terminal in the root directory of the project, and run the following commands:

```
pip install -r requirements.txt
```

This will ensure that all the dependencies for the documentation build are installed.

Once inside of the `docs` directory, the documentation site can be built with the following commands:

```
./make.bat html
```

From here, the website can be loaded by opening the `index.html` page in a web browser, which is located within the `docs/build/html` directory.

## Contributing Guidelines

Contributing to the documentation is easy. First, *create a branch* in the current repository, titled with the preface `docs_`, followed by the features or branch name for what you plan on adding.

Once your work is complete, verify that the `build-test` CI script is able to execute successfully, and submit a merge request into the `main` branch.