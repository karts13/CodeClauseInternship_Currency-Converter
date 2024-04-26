from exchange_rates import exchange_rates

def currency_converter(amount, from_currency, to_currency):
    if from_currency not in exchange_rates or to_currency not in exchange_rates:
        return "Invalid currency code"

    exchange_rate = exchange_rates[from_currency][to_currency]
    converted_amount = amount * exchange_rate
    return converted_amount