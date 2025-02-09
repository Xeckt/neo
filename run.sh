#!/bin/bash

if ! type poetry > /dev/null; then
  echo "cannot find the poetry command, is it installed?"
fi

poetry install
poetry run python bot/main.py
