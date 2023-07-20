# Checks input is a number more than a given value
def num_check(question, low):
    # checks if the user entered a number that is more than zero
    valid = False
    while not valid:

        error = "Please enter a integer with no decimal points (or equal to) {} ".format(low)

        try:

            # asks user to enter a number
            response = int(input(question))

            # checks if a number is above zero
            if response >= low:
                return response

            # outputs error if number is invalid
            else:
                print(error)
                print()

        except ValueError:
            print(error)

# Converts decimal to binary and states how
# Many bits are needed to represent the original integer
def int_bits():

    # Get integer (must be >=0)
    var_integer = num_check("Please enter an integer", 0)

    var_binary = "{0:b}".format(var_integer)

    # Calculates # of bits (length of string above)
    num_bits = len(var_binary)

        # Output answer with working out
    print()
    print("{} in binary is {}".format(var_integer, var_binary))
    print("# of bits is {}".format(num_bits))
    print()

    return ""

# Main routine
int_bits()