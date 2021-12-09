# ChessEngine Documentation

**Documentation Website**: https://nathandupont.github.io/ChessEngine/

This section is dedicated to explaining the ChessEngine documentation website, as well as outline how to contribute to the documentation. 

This website was created to outline how to use the Chess engine, and outline the features available within the source code. This documentation is a living document, and allows expansion to help capture the use cases of the code in this repository.

Information below will be *specific to viewing and modifying the documentation*.

## Getting Started

Ensure that the *Getting Started* steps of the `README` in the root have been completed before starting this section.

Open a bash terminal and change directors to the `docs` directory. From here, the documentation site can be built with the following commands:

```
./make.bat html
```

The website can be loaded by opening the `index.html` page in a web browser, which is located within the `docs/build/html` directory.

## Contributing Guidelines

Contributing to the documentation is easy. First, *create a branch* in the current repository, titled with the preface `docs_`, followed by the features or branch name for what you plan on adding.

Once your work is complete, verify that the `build-test` CI script is able to execute successfully, and submit a merge request into the `main` branch.