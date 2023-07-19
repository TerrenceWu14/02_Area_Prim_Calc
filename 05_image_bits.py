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


# Finds # of bits for 24 bit colour
def image_bits():
    # Asks user for Width and Height of the Image
    image_height = num_check("Image Height:", 1)
    image_width = num_check("Image Width:", 1)
    # Calculates # of Bits and Pixels
    image_pixels = image_height * image_width
    image_bits = image_pixels * 24

    # Outputs the answer
    print()
    print("# of pixels = {} x {} = {}".format(image_height, image_width, image_pixels))

    print("# of bits = {} x 24= {}".format(image_pixels, image_bits))
    print()

    return ""

# Main routine goes here
image_bits()
