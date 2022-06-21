# first stage
FROM python:3.8 AS builder
COPY requirements.txt .

# install dependencies
RUN pip install --user -r requirements.txt

# second stage
FROM python:3.8-slim
#WORKDIR /code

RUN mkdir /app
WORKDIR /app

COPY --from=builder /root/.local /root/.local
COPY ./src/alphavantage-flask.py /app/

# update PATH environment variable
ENV PATH=/root/.local:$PATH

# Exposing Ports
EXPOSE 5000

CMD [ "python", "/app/alphavantage-flask.py" ]