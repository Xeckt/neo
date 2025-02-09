# Setting up Neo
Neo uses `Poetry` for it's package / dependency management. You can 
[visit the poetry website](https://python-poetry.org/docs/) to install it.

After it is installed, setup the project:

1. Run `poetry install` to install the project dependencies
2. It is recommended to run `poetry sync` every once in the while to ensure continuity with the `poetry.lock` file

Finally, you can run the project from the root of the project, not from inside the `neo` folder:
```commandline
poetry run python neo/main.py
```
Alternatively you can run the `run.sh` script to start it. 