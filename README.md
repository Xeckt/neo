# Requirements
Check [requirements.txt](https://github.com/pritam42069/yadps-chan/blob/main-(stable)/requirements.txt)

# Description
- YADPS-Chan Version: `0.0.4`
- This project isn't maintained consistently, it's a hobby learning project by our server to work on as time goes on.

# Roadmap
 * [x] Create basic logging system
 * [x] Create bot configuration system
 * [x] Create modular command system
 * [x] Create docker build images and docker-compose for launching the bot
 * [x] Create project setup ready for contributions
 * [ ] Backend bot interface

# Key features
- As stated in the description, a very modular system to use and design with
- Beginner-friendly
- Useful base features

# Installation & Setup
## Standard
1. [First install minimum Python 3.10](https://www.python.org/downloads/)
2. Install requirements via `pip install -r requirements.txt`
3. Setup `.env` file inside `settings/` folder with key value `TOKEN=XXX`
4. Run `python __main__.py` 
5. For some systems it may be `python3` instead of `python`

## Docker
1. This guide is under the presumption you have Docker installed.
2. Setup `.env` file inside `settings/` folder with key value `TOKEN=XXX`
3. It is heavily suggested to use `compose v2` which can be [installed from official Docker documentation](https://docs.docker.com/compose/cli-command/)
4. Run the following command: `docker build -t "yadps:latest" .` to build the image `yadps:latest`
5. Using `v2 compose` to run the bot: `docker compose up` in the same location as `docker-compose.yml`

## General tips

# Contributing
- You can fork the repository and make a pull request with your changes if you want to contribute.
- A `CONTRIBUTING.md` file will be created for future contributions
- Most of the decisions regarding the bot are taken on [this Discord server](https://discord.gg/zFBfXDY7RY)
