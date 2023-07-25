# Functions goes here

# Put series of symbols at start and end of text (for emphasis)
def statement_generator(text, decoration):
    # Make string with five characters
    ends = decoration * 5

    # Add decoration to start and end of statement
    statement = "{} {} {}".format(ends, text, ends)

    print()
    print(statement)
    print()

    return ""


# Displays Instructions / Information
def instructions():
    statement_generator("Instructions / Information", "=")
    print()
    print(" Please choose a data type (image / text / integer)")
    print()
    print("This program assumes that images are being represented in 24 bit color (ie: 24 bits per pixel). "
          "For text we assume that ascii encoding is being used (8 bits per character)")
    print()
    print("Complete as many calculations as necessary, "
          "pressing <enter> at the end of each calculator or any key to quit.")
    print()
    return ""


# Checks user choice is 'integer', 'text' or 'image'
def user_choice():
    valid = False

    while not valid:
        # asks user for choice and change response to lowercase
        response = input("File type (integer / text / image):").lower()

        # Lists of valid responses
        text_ok = ["text", "t", "txt"]
        integer_ok = ["integer", "int", "#" "number"]
        image_ok = ["image", "img", "pix", "picture", "pic", "p"]

        # Checks for valid response and returns text, integer or image
        if response in text_ok:
            return "text"
        elif response in integer_ok:
            return "integer"
        elif response in image_ok:
            return "image"
        elif response == "i":
            want_integer = input("Press <enter> for an image or any key for an integer: ")

            if want_integer == "":
                return "image"
            else:
                return "integer"

        else:
            # if response is not valid, output an error
            print("Sorry, please choose integer, text or image")
            print()


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


# Calculates the # of bits for the text (# of characters x 8)
def text_bits():
    # Asks user for a string
    var_text = input("Enter some text: ")

    # Calculates # of bits (length of string x 8)
    var_length = len(var_text)
    num_bits = 8 * var_length

    # Output answer with working
    print()
    print("\'{}\' has {} characters ...".format(var_text, var_length))
    print("# of bits is {} x 8 ...".format(var_length))
    print("We need {} bits to represent {}".format(num_bits, var_text))
    print()

    return ""


# Finds # of bits for 24 bit color
def image_bits():
    # Asks user for Width and Height of the Image
    img_height = num_check("Image Height:", 1)
    image_width = num_check("Image Width:", 1)
    # Calculates # of Bits and Pixels
    image_pixels = img_height * image_width
    img_bits = image_pixels * 24

    # Outputs the answer
    print()
    print("# of pixels = {} x {} = {}".format(img_height, image_width, image_pixels))

    print("# of bits = {} x 24= {}".format(image_pixels, img_bits))
    print()

    return ""


# Converts decimal to binary and states how
# Many bits are needed to represent the original integer
def int_bits():
    # Get integer (must be >=0)
    var_integer = num_check("Please enter an integer:", 0)

    var_binary = "{0:b}".format(var_integer)

    # Calculates # of bits (length of string above)
    num_bits = len(var_binary)

    # Output answer with working out
    print()
    print("{} in binary is {}".format(var_integer, var_binary))
    print("# of bits is {}".format(num_bits))
    print()

    return ""

# Main routine goes here

# Heading
statement_generator("Bit Calculator for Integers, Text & Images", "-")

# Display instructions if user has not used the program before
first_time = input("Press <enter> to see the instructions or any key to continue")

if first_time == "":
    instructions()
# Loop to allow multiple calculations per session
keep_going = ""
while keep_going == "":

    # Ask the user for the file type
    data_type = user_choice()
    print("You chose", data_type)

    # Ask the user for the file type
    if data_type == "integer":
        int_bits()

    # For images, ask for width and height
    # (Must be integers more than / equal to 1)
    elif data_type == "image":
        image_bits()

    # For text, ask for a string
    else:
        text_bits()

        print()

    keep_going = input("Press <enter> to continue or any other key to quit")
    print()
