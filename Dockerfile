FROM python:3.10

WORKDIR /usr/src/app

COPY . .

RUN pip install --no-cache-dir -r Requirements.txt

ENTRYPOINT ["python", "./server.py"]