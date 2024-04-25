from exchange_rates import exchange_rates

def currency_converter(amount, from_currency, to_currency):
    if from_currency not in exchange_rates or to_currency not in exchange_rates:
        return "Invalid currency code"

    exchange_rate = exchange_rates[from_currency][to_currency]
    converted_amount = amount * exchange_rate
    return converted_amount

def main():
    print("Welcome to Currency Converter")
    print("Available currencies: USD, EUR, GBP, JPY, INR, etc.")

    amount = float(input("Enter the amount to convert: "))
    from_currency = input("Enter the currency to convert from: ").upper()
    to_currency = input("Enter the currency to convert to: ").upper()

    converted_amount = currency_converter(amount, from_currency, to_currency)
    if isinstance(converted_amount, str):
        print(converted_amount)
    else:
        print(f"{amount} {from_currency} is equal to {converted_amount} {to_currency}")

if __name__ == "__main__":
    main()