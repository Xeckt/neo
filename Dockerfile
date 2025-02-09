FROM python:3.10
COPY neo/ /usr/src/app
WORKDIR /usr/src/app
RUN python -m pip install --editable .
CMD [ "python", "main.py" ]