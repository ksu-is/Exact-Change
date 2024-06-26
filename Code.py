def calculate_change(cost, amount_paid):
    change = round(amount_paid - cost, 2)

    change_in_cents = int(change * 100)

    quarters = change_in_cents // 25
    change_in_cents %= 25

    dimes = change_in_cents // 10
    change_in_cents %= 10

    nickels = change_in_cents // 5
    change_in_cents %= 5

    pennies = change_in_cents

    return quarters, dimes, nickels, pennies

def main():
    while True:
        try:
            cost = float(input("Enter the cost: $"))
            amount_paid = float(input("Enter the amount paid: $"))
            
            if amount_paid < cost:
                print("The amount paid must be greater than or equal to the cost. Please try again.")
                continue
            
            quarters, dimes, nickels, pennies = calculate_change(cost, amount_paid)
            print(f"Change: {quarters} quarters, {dimes} dimes, {nickels} nickels, {pennies} pennies")
            
            break
        except ValueError:
            print("Invalid input. Please enter numerical values.")

if __name__ == "__main__":
    main()
