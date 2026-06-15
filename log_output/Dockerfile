FROM python:3.12-slim

WORKDIR /app

COPY app ./app

RUN useradd -m appuser
USER appuser

CMD ["python", "-u", "app/main.py"]
