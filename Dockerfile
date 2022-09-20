FROM python:3.10-slim-buster

WORKDIR /usr/src

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD ["uvicorn", "server:app", "--host=0.0.0.0", "--reload", "--log-level=info"]
