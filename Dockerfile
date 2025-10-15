FROM python:3.12-slim

WORKDIR /app

COPY app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app/ /app/

RUN useradd --create-home --shell /bin/bash appuser
USER appuser

EXPOSE 5000
CMD ["python", "main.py"]

