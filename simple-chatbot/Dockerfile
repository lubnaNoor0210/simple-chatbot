FROM python:3.10-slim

WORKDIR /app
COPY . .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ["chainlit", "run", "app.py", "--port", "7860", "--host", "0.0.0.0"]
