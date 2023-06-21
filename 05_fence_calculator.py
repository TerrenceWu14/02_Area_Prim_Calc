# functions go here

# checks input is a number more than zero
def num_check(question):
    valid = False
    while not valid:
        
        error = "Please enter a number that is more than zero"
        
        try:
        
            # ask user to enter a number
            response = float(input(question))
            
            # checks number is more than zero
            if response > 0:
                return response
            
            # outputs error if input is invalid
            else:
                print(error)
                print()
                
        except ValueError:
            print(error)    
    


# Main Routine goes here


# Introduction / Heading print statements
print()
print("**** Fence Cost Calculator ****")
print()

# Start of calculator loop
keep_going = ""
while keep_going == "":
   # Call your number checker function three times to get the width, length and cost_per_meter of the fencing
    print("What is the width, length and cost of fencing per meter? ")
    width = num_check("Width: ")
    length = num_check("Length: ")
    price = num_check("Price Per Meter: ")
    # Calculate perimeter (width + height) x 2
    perimeter = (width + length) * 2
    # Calculate the cost of the fencing (perimeter x price / meter)
    cost_of_fencing = perimeter * price


# Output the perimeter and cost of the fencing
print("Perimeter: {:.2f} units" .format(perimeter))
print("Cost: {:.2f} units" .format(cost_of_fencing))


keep_going = input("Press <enter> to keep going or any key to quit")
    
print("- * 30")
print("Thanks for using the Fencing cost calculator")

        
    
    