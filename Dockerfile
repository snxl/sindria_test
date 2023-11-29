FROM python:3.12-alpine

WORKDIR /app
COPY requirements.txt .

RUN pip3 install -r requirements.txt

EXPOSE 5000

COPY . /app

ENTRYPOINT ["python3", "-m", "src.server"]