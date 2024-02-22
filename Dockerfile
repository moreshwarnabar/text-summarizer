FROM python:3.8-slim-buster

RUN apt update -y && apt install awscli -y
WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt
RUN pip install --updgrade accelerate
RUN pip uninstall -y transformers accelerate
RUN pip intall transformers accelerate

CMD ["python3", "app.py"]