"""
Assignment 6
Challenge: Allow the user to choose from multiple currency pairs and implement appropriate error handling for invalid currency inputs.
==============================================
Input: Ask the user to enter an amount in one currency (e.g., USD).
Processing: Convert the amount to another currency (e.g., EUR) using a fixed exchange rate.
Output: Display the converted amount in the target currency.

Placid Auguste - 9/23/2024
"""

# MyFunction:
def usd_to_euro(usd_amount, exchange_rate):
    euro_amount = usd_amount * exchange_rate

# Exchange Rate
exchange_rate = 0.85

# Input:
usd_amount = float(input("Enter the amount US Dollars you want to convert: "))

# Processing:
euro_amount = usd_amount * exchange_rate

# Output:
txt = (f"${usd_amount:.2f} (US Dollars) is equivalent to €{euro_amount:.2f} (EUROS).")
print('\n')
print(txt)
