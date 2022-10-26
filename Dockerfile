FROM python:3.8 as gdown

WORKDIR /drive

RUN pip install gdown && gdown --folder 1q8YEYfueLgoXO9SewZ2DxKutZfwVBqz8 -O models 

COPY static ./
COPY templates ./
COPY *.py ./

FROM python:3.8.15

WORKDIR /app

COPY requirements.txt ./
COPY --from=gdown /drive ./

RUN pip install --upgrade pip && \
    pip install -r requirements.txt

CMD ["python", "web.py"]