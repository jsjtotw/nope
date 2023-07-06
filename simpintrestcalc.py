def calculate_simple_interest(principle, rate, time):
    interest = (principle * rate * time) / 100
    return interest
def main():
    while True:
        print("Select the mode:")
        print("1. Calculate interest")
        print("2. Calculate principle")
        print("3. Calculate principle + interest")
        print("4. Calculate rate")
        print("5. Calculate time")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            principle = float(input("Enter the principle amount: "))
            rate = float(input("Enter the interest rate: "))
            time = float(input("Enter the time (in years): "))

            interest = calculate_simple_interest(principle, rate, time)
            print("The interest is:", interest)
        elif choice == "2":
            interest = float(input("Enter the interest: "))
            rate = float(input("Enter the interest rate: "))
            time = float(input("Enter the time (in years): "))

            principle = interest / (rate * time / 100)
            print("The principle amount is:", principle)
        elif choice == "3":
            interest = float(input("Enter the interest: "))
            rate = float(input("Enter the interest rate: "))
            time = float(input("Enter the time (in years): "))

            principle = interest / ((rate * time / 100) + 1)
            print("The principle + interest amount is:", principle + interest)
        elif choice == "4":
            principle = float(input("Enter the principle amount: "))
            interest = float(input("Enter the interest: "))
            time = float(input("Enter the time (in years): "))

            rate = (interest / (principle * time)) * 100
            print("The interest rate is:", rate)
        elif choice == "5":
            principle = float(input("Enter the principle amount: "))
            interest = float(input("Enter the interest: "))
            rate = float(input("Enter the interest rate: "))
            time = interest / (principle * rate / 100)
            print("The time (in years) is:", time)
        elif choice == "6":
            print("Exiting the program...")
            break
        else:
            print("Invalid choice! Please enter a number from 1 to 6.")
        print()  # Print a blank line for readability
if __name__ == "__main__":
    main()
