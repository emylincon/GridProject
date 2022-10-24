FROM python:3.8.15

WORKDIR /app

COPY /static /static
COPY /templates /templates
COPY *.py .
COPY requirements.txt .

RUN pip install -r requirements.txt

CMD ["python3" "web.py"]