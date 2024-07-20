FROM python:3.11.9-slim

WORKDIR /app

# Install netcat-openbsd
RUN apt-get update && apt-get install -y netcat-openbsd

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

# Ensure the script has the right permissions
RUN chmod +x /app/entrypoint.sh

EXPOSE 5000

ENV FLASK_APP=app:create_app
ENV FLASK_ENV=development
