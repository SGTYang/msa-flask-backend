FROM python:3.7.7-slim

WORKDIR /
COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY details.py /microservices/
COPY requirements.txt /microservices/

WORKDIR /microservices
EXPOSE 4321

CMD ["python", "details.py", "4321"]
