from tkinter import *
from forex_python.converter import CurrencyRates

# Create window
root = Tk()
root.title("Currency Converter")
root.geometry("350x250")
root.config(bg="#f1f1f1")

# Currency converter
cr = CurrencyRates()

# Functions
def convert_currency():
    try:
        amount = float(entry_amount.get())
        from_curr = entry_from.get().upper()
        to_curr = entry_to.get().upper()
        result = cr.convert(from_curr, to_curr, amount)
        label_result.config(text=f"{amount} {from_curr} = {round(result, 2)} {to_curr}")
    except Exception as e:
        label_result.config(text="Error: " + str(e))

# UI Components
Label(root, text="Amount:", bg="#f1f1f1").pack(pady=5)
entry_amount = Entry(root, width=20)
entry_amount.pack()

Label(root, text="From Currency (e.g. USD):", bg="#f1f1f1").pack(pady=5)
entry_from = Entry(root, width=20)
entry_from.pack()

Label(root, text="To Currency (e.g. INR):", bg="#f1f1f1").pack(pady=5)
entry_to = Entry(root, width=20)
entry_to.pack()

Button(root, text="Convert", command=convert_currency, bg="#4CAF50", fg="white").pack(pady=10)

label_result = Label(root, text="", bg="#f1f1f1", font=("Arial", 12))
label_result.pack()

root.mainloop()