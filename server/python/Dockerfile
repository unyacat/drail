FROM python:3-alpine

COPY . .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ["python3", "main.py"]