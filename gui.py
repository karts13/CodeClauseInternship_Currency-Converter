import tkinter as tk
from SwiftSwitch import currency_converter

class CurrencyConverterApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Currency Converter")

        self.amount_label = tk.Label(self, text="Amount:")
        self.amount_label.grid(row=0, column=0)
        self.amount_entry = tk.Entry(self)
        self.amount_entry.grid(row=0, column=1)

        self.from_currency_label = tk.Label(self, text="From Currency:")
        self.from_currency_label.grid(row=1, column=0)
        self.from_currency_entry = tk.Entry(self)
        self.from_currency_entry.grid(row=1, column=1)

        self.to_currency_label = tk.Label(self, text="To Currency:")
        self.to_currency_label.grid(row=2, column=0)
        self.to_currency_entry = tk.Entry(self)
        self.to_currency_entry.grid(row=2, column=1)

        self.convert_button = tk.Button(self, text="Convert", command=self.convert)
        self.convert_button.grid(row=3, columnspan=6)

        self.result_label = tk.Label(self, text="")
        self.result_label.grid(row=4, columnspan=6)
        self.result_label.grid(row=4, columnspan=6)

    def convert(self):
        amount = float(self.amount_entry.get())
        from_currency = self.from_currency_entry.get().upper()
        to_currency = self.to_currency_entry.get().upper()

        converted_amount = currency_converter(amount, from_currency, to_currency)
        if isinstance(converted_amount, str):
            self.result_label.config(text=converted_amount)
        else:
            self.result_label.config(text=f"{amount} {from_currency} is equal to {converted_amount} {to_currency}")

if __name__ == "__main__":
    app = CurrencyConverterApp()
    app.mainloop()