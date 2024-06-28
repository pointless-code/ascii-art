# Use an official Python runtime as a parent image
FROM python:3.9-slim

WORKDIR /usr/src/app

COPY . .

CMD ["python", "./ascii_art.py"]
