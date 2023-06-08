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
width = num_check("Width: ")
height = num_check("Height: ")

# calculate the area (width x height)
area = width * height

# calculate the perimeter (width + height) x 2
perimeter = 2 * (width + height)

# Output area and perimeter
print("Perimeter: {} units" .format(perimeter))
print("Area: {} units" .format(area))3