FROM python:3.11.2

WORKDIR /python-docker
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY LoanCalculator.py LoanCalculator.py
EXPOSE 5000

CMD ["python", "LoanCalculator.py"]
