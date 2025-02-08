FROM python:3.10
COPY bot/ /usr/src/app
WORKDIR /usr/src/app
RUN python -m pip install --editable .
CMD [ "python", "main.py" ]