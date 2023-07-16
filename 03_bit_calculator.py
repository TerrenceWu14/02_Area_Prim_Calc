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
    # Must be an integer more than / equal to 0

    # For images, ask for width and height
