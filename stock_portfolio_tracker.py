# Stock Portfolio Tracker
# CodeAlpha Python Programming Internship - Task 2

print("===== STOCK PORTFOLIO TRACKER =====")

stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 300,
    "AMZN": 170
}

portfolio = []
total_investment = 0

while True:
    ticker = input("\nEnter stock ticker (or 'done' to finish): ").upper()

    if ticker == "DONE":
        break

    if ticker not in stock_prices:
        print("Sorry, that ticker is not available. Try again.")
        continue

    quantity_input = input("Enter quantity: ")

    if not quantity_input.isdigit():
        print("Please enter a valid whole number for quantity.")
        continue

    quantity = int(quantity_input)
    price = stock_prices[ticker]
    investment = price * quantity

    portfolio.append([ticker, quantity, price, investment])
    total_investment = total_investment + investment

print("\n===== YOUR PORTFOLIO =====")
print(f"{'Stock':<10}{'Quantity':<12}{'Price':<10}{'Value':<10}")

for holding in portfolio:
    stock = holding[0]
    qty = holding[1]
    price = holding[2]
    value = holding[3]
    print(f"{stock:<10}{qty:<12}${price:<9}${value:<9}")

print("-" * 40)
print(f"TOTAL INVESTMENT VALUE: ${total_investment}")

save_choice = input("\nDo you want to save this to a file? (yes/no): ").lower()

if save_choice == "yes":
    with open("portfolio.txt", "w") as file:
        file.write("===== YOUR PORTFOLIO =====\n")
        file.write(f"{'Stock':<10}{'Quantity':<12}{'Price':<10}{'Value':<10}\n")

        for holding in portfolio:
            stock = holding[0]
            qty = holding[1]
            price = holding[2]
            value = holding[3]
            file.write(f"{stock:<10}{qty:<12}${price:<9}${value:<9}\n")

        file.write("-" * 40 + "\n")
        file.write(f"TOTAL INVESTMENT VALUE: ${total_investment}\n")

    print("Portfolio saved to portfolio.txt")
else:
    print("Portfolio not saved.")