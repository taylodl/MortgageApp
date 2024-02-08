from decimal import Decimal, ROUND_HALF_UP
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/loancalculator')
def loanCalculator() :
    months_str = request.args.get('months')
    amount_str = request.args.get('amount')
    apr_str = request.args.get('apr')

    try:
        months = int(months_str)
        amount = float(amount_str)
        apr = float(apr_str)
    except ValueError:
        return {'error' : 'Values must be numeric'}, 400 

    #return jsonify({"months" : months, "amount" : amount, "apr" : apr})
    return jsonify(create_loan_payment_data(months, amount, apr))

@app.route('/testing')
def test() :
    return 'This is a test'

def create_loan_payment_data(months, principal, interest_rate) :
    # Validate inputs
    if (not isinstance(months, int) or months < 1) :
        return {"error" : "months must be a whole number >= 1"}
    if (not (principal > 0)) :
        return {"error" : "principal must be greater than 0"} 
    if (not (interest_rate > 0)) :
        return {"error" : "interest rate must be greater than 0"}

    # Initialize our data to return
    ReturnedData = {}
    LoanData = {"Monthly Payment" : 0, "Payments" : 0, "Total Interest" : 0, "Total Loan Cost" : 0}
    PaymentData = []

    # Preliminary calculations to get us started

    # The interest rate given is APY, we need to turn to an actual percentage and divide by 12 to get a monthly percentage
    monthly_rate = Decimal(interest_rate / 100 / 12)
    
    # Consideration: we're working with currency, not floats.
    # We need to work with Decimal and round up to the nearest cent (typical strategy in finance - check assumption with client)

    # This is the formula provided by the client to calculate the monthly payment
    principal = Decimal(principal)
    monthly_payment = principal * monthly_rate * ((1 + monthly_rate) ** months) / (((1 + monthly_rate) ** months) - 1)
    monthly_payment = Decimal(monthly_payment).quantize(Decimal('0.01'))
        
    # Initialize LoanData values
    total_interest_paid = Decimal(0.00)
    total_loan_cost = Decimal(0.00)
    remaining_loan_balance = Decimal(principal)

    # Now let's go through the months
    for month in range(1, months + 1) :
        monthly_interest = (remaining_loan_balance * monthly_rate).quantize(Decimal('0.01'))
        monthly_principal = (monthly_payment - monthly_interest).quantize(Decimal('0.01'))
        remaining_loan_balance = (remaining_loan_balance - monthly_principal).quantize(Decimal('0.01'))
        total_interest_paid = (total_interest_paid + monthly_interest).quantize(Decimal('0.01'))
        beginning_balance = (remaining_loan_balance + monthly_principal).quantize(Decimal('0.01'))
        total_loan_cost = (total_loan_cost + monthly_payment).quantize(Decimal('0.01'))

        PaymentData.append({"Month" : month, 
                         "Beginning Balance" : f"{beginning_balance:.2f}",
                         "Payment" : f"{monthly_payment:.2f}", 
                         "Principal" : f"{monthly_principal:.2f}",
                         "Interest" : f"{monthly_interest:.2f}",
                         "Ending Balance" : f"{remaining_loan_balance:.2f}"})

    # Now let's package the results
    LoanData["Monthly Payment"] = f"{float(monthly_payment):.2f}"
    LoanData["Payments"] = months
    LoanData["Total Interest"] = f"{float(total_interest_paid):.2f}"
    LoanData["Total Loan Cost"] = f"{float(total_loan_cost):.2f}"

    ReturnedData = {"Loan Data" : LoanData, "Payment Data" : PaymentData}

    return ReturnedData


if __name__ == '__main__':
    app.run(debug=True)

