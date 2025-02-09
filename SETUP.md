# Setting up Neo
Neo uses `Poetry` for it's package / dependency management. You can
[visit the poetry website](https://python-poetry.org/docs/) to install it.

After it is installed, setup the project:

1. Run `poetry install` to install the project dependencies
2. It is recommended to run `poetry sync` every once in the while to ensure continuity with the `poetry.lock` file
3. Finally, go into the `bot` directory and `poetry run neo`
