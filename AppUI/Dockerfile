FROM python:3.11.2

WORKDIR /python-docker
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY LoanAppUI.py /python-docker/LoanAppUI.py
COPY ./templates /python-docker/templates

ENV SERVICE_URL="http://localhost:5080/loancalculator"

EXPOSE 80

CMD ["python", "LoanAppUI.py"]
