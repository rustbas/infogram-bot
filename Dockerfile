FROM python:3.11-alpine

WORKDIR /app
COPY requirements.txt .
COPY main.py .

RUN pip install -r requirements.txt

ENTRYPOINT [ "python3", "main.py" ]
