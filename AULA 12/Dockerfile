FROM python:3.14.3-slim

LABEL maintainer="mapatagorda@gmail.com"

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["python", "app.py"]