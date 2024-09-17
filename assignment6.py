# Function to convert USD to EUR
def convert_usd_to_eur(usd_amount, exchange_rate):
    eur_amount = usd_amount * exchange_rate
    return eur_amount

# Fixed exchange rate (example: 1 USD = 0.85 EUR)
exchange_rate = 0.85

# Input: Ask user to enter the amount in USD
usd_amount = float(input("Enter the amount in USD: "))

# Processing: Convert USD to EUR
eur_amount = usd_amount * exchange_rate

# Output: Display the converted amount in EUR
print(f"{usd_amount} USD is equivalent to {eur_amount:.2f} EUR.")
