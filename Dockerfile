FROM python:3.11

WORKDIR /app

COPY requirements.txt .
RUN apt update && apt install -y curl
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "app/main.py"]
