# Build the UI
cd ./AppUI
docker build --tag loan-calculator-ui .

# Build the app services tier
cd ../ServiceAPI
docker build --tag loan-calculator-api .

# Buid the data services tier
cd ../DataAPI
docker build --tag loan-calculator-data .
