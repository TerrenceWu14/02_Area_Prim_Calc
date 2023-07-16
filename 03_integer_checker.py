# Checks input is a number more than a given value

def num_check(question, low):
    # checks if the user entered a number that is more than zero
    valid = False
    while not valid:

        error = "Please enter a integer that is more than "
        "(or equal to) {}".format(low)

        try:

            # asks user to enter a number
            response = int(input(question))

            # checks if a number is above zero
            if response > low:
                return response

            # outputs error if number is invalid
            else:
                print(error)
                print()

        except ValueError:
            print(error)