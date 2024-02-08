from flask import Flask, render_template, request
from decimal import Decimal
import requests
import os

app = Flask(__name__)

loan_calculator_service_url = os.environ.get("SERVICE_URL")

# Function to get loan data (wraps the API call)
def get_loan_payment_data(months, amount, apr) : 
    params = {'months': months, 'amount': amount, 'apr': apr}
    print(f"loan_calculator_service_url = {loan_calculator_service_url}")
    response = requests.get(loan_calculator_service_url, params)
    if response.status_code == 200:
        return response.json()
    else:
        return {}
    

# Our default route goes to the application UI
@app.route('/')
def index() :
    return render_template('index.html')


# Route to handle form submission, i.e. process inputs, then get and display the results
@app.route('/calculate', methods=['POST'])
def calculate_loan() :
    months = int(request.form['months'])
    amount = Decimal(request.form['amount']).quantize(Decimal('0.01'))
    apr = Decimal(request.form['apr']).quantize(Decimal('0.01'))
    loan_payment_data = get_loan_payment_data(months, amount, apr)
    if "error" in loan_payment_data:
        return render_template('error.html', loan_payment_data = loan_payment_data)
    else:
        return render_template('loandetails.html', loan_payment_data = loan_payment_data)

if __name__ == '__main__' :
    app.run(host='0.0.0.0', port=80)
