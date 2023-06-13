# function goes here

# checks input is a number more than zero
def num_check(question):
    # checks if the user entered a number that is more than zero
    valid = False
    while not valid:

        error = "Please enter a number that is more than zero"

        try:

            # asks user to enter a number
            response = float(input(question))

            # checks if a number is above zero
            if response > 0:
                return response

            # outputs error if number is invalid
            else:
                print(error)
                print()

        except ValueError:
            print(error)


# Main routine goes here

# Introduction / Heading print statements
print()
print("*** Area Perimeter Calculator***")
print()
keep_going = ""
while keep_going == "":

    width = num_check("Width: ")
    height = num_check("Height: ")

    # calculate the area (width x height)
    area = width * height

    # calculate the perimeter (width + height) x 2
    perimeter = 2 * (width + height)

    # Output area and perimeter to 2 decimal places
    print("Perimeter: {:.2f} units" .format(perimeter))
    print("Area: {:.2f} units" .format(area))

    keep_going = input("Press <enter> to keep going or any key to quit")

    print()
    print("Thanks for using the area / perimeter calculator")