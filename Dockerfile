# syntax=docker/dockerfile:1
FROM python:3.11
WORKDIR /app
COPY requirements.txt /app/requirements.txt
RUN pip3 install -r requirements.txt
COPY . /app
CMD ["python", "-m" , "motor.py"]
EXPOSE 8000
