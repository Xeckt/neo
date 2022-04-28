FROM python:3.10
COPY . /directory/of/bot
WORKDIR /same/as/above/dir
RUN python -m pip install --editable .
COPY . .
CMD [ "python", "main.py" ]