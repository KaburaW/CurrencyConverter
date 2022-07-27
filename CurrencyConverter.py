rates = {"USD": {"KSH": 1 / 112.50, "EUR": 1.20},
         "EUR": {"KSH": 1 / 132.45, "USD": 1 / 1.20},
         "KSH": {"USD": 112.50, "EUR": 132.45}}

print('''Welcome to your currency converter.

          ''')

try:
    currencyFrom = input('Enter the currency you would like to convert from: ').upper()
    currencyTo = input('Enter the currency you would like to convert to: ').upper()
    amount = float(input('Enter the amount you want to convert: '))
    conversion = amount * rates[currencyTo][currencyFrom]

    if currencyFrom == "USD" and (currencyTo == "KSH" or "EUR"):
        print("%.2f" % conversion)

    elif currencyFrom == "EUR" and (currencyTo == "KSH" or "USD"):
        print("%.2f" % conversion)

    elif currencyFrom == "KSH" and (currencyTo == "USD" or "EUR"):
        print("%.2f" % conversion)

except ValueError:
    print("Amount Value Error. Please try again")

except KeyError:
    print("Currency Error. Please try again")
