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

    return""


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
            want_integer = input("Press <enter> for an inter or any key for an image: ")

            if want_integer == "":
                return "integer"
            else:
                return "image"

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


# Main routine goes here

# Heading
statement_generator("Bit Calculator for Integers, Text & Images", "-")

# Display instructions if user has not used the program before

# Loop to allow multiple calculations per session
keep_going = ""
while keep_going == "":

    #Ask the user for the file type
    data_type = user_choice()
    print("You chose", data_type)

    # For integer, ask for integer
    if data_type =="integer":
        var_integer = num_check("enter an integer:", 0)
    # For images, ask for width and height
    # Must be an integer more than / equal to 1
    elif data_type == "image":
        image_width = num_check ("Image width?", 1)
        print()
        image_height = num_check("Image height? ", 1)

    # For text, ask for a string
    else:
        var_text = input("Enter some text: ")

