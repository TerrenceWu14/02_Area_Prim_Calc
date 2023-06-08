# checks if the user entered a number that is more than zero
valid = False
while not valid:

    error = "Please enter a number that is more than zero"

    try:

        # asks user to enter a number
        response = float(input("Enter a number: "))

        # checks if a number is above zero
        if response > 0:
            valid = True

        # outputs error if number is invalid
        else:
            print(error)
            print()

    except ValueError:
        print(error)

