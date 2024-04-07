# Write a program that takes cost price and selling price as user input and determines whether it's a loss, profit, or neither.

def determine_profit_or_loss(cost_price, selling_price):
    if selling_price > cost_price:
        return "profit"
    elif selling_price < cost_price:
        return "loss"
    else:
        return "neither"


def main():
    while True:
        try:
            cost_price = float(input("Enter the cost price: "))
            selling_price = float(input("Enter the selling price: "))
            break
        except ValueError:
            print("Please enter valid numbers.")

    result = determine_profit_or_loss(cost_price, selling_price)

    if result == "profit":
        print(
            f"The selling price of {selling_price} is greater than the cost price of {cost_price}, resulting in a profit.\n"
            f"You got {selling_price - cost_price} profit.")
    elif result == "loss":
        print(
            f"The selling price of {selling_price} is less than the cost price of {cost_price}, resulting in a loss.\n"
            f"You are losing {selling_price - cost_price}"
        )
    else:
        print(
            f"The selling price of {selling_price} is equal to the cost price of {cost_price}, resulting in neither a profit nor a loss.")


if __name__ == "__main__":
    main()
