# Dockerfile
FROM python:latest
WORKDIR /srv
RUN pip install --upgrade pip
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . /srv
ENV FLASK_APP=app
CMD ["python","app.py"]