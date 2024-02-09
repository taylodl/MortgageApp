FROM python:3.11.2

WORKDIR /python-docker
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY LoanAppCache.py LoanAppCache.py

EXPOSE 5000

CMD ["python", "LoanAppCache.py"]