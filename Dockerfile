FROM python:3.7-alpine
RUN pip install --no-cache-dir pytest

WORKDIR /app

COPY tests tests
COPY *.py ./

CMD ["python", "main.py"]

