try:
    num_1 = int(input("Enter the First Number: "))
    num_2 = int(input("Enter the Second Number: "))

    print("\nChoose calculation to perform:")
    print("add")
    print("subtract")
    print("multiply")
    print("divide")

    cal = input("Enter operation: ").strip().lower()

    if cal == "add":
        ans = num_1 + num_2
    elif cal == "subtract":
        ans = num_1 - num_2
    elif cal == "multiply":
        ans = num_1 * num_2
    elif cal == "divide":
        if num_2 == 0:
            print("Error! Can't divide by zero.")
            ans = None
        else:
            ans = num_1 / num_2
    else:
        print("Invalid Operation!")
        ans = None

    if ans is not None:
        print(f"The Answer is: {ans}")

except ValueError:
    print("Invalid Input! Please enter valid numbers.")
