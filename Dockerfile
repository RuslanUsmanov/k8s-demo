FROM python:3.12-alpine

WORKDIR /code

COPY ./* /code/

RUN pip install -r requirements.txt --no-cache-dir

CMD ["uvicorn", "--host", "0.0.0.0", "--port", "80", "main:app"]
