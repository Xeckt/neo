# Setting up Neo
Neo uses `Poetry` for it's package / dependency management. You can
[visit the poetry website](https://python-poetry.org/docs/) to install it.

After it is installed, setup the project:

1. Go to `./bot/conf` and adjust `neo.yaml` accordingly
2. Create aN `.env` inside `conf/` folder and place your token `TOKEN="..."`
3. Run `poetry install` to install the project dependencies, then `poetry -C ./bot run neo` from the project root

It is recommended to run `poetry sync` every once in the while to ensure continuity with the `poetry.lock` file
