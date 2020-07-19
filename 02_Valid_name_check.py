import math

# Checks a response to a question is not blank and no number in it
def not_blank (question):
    error = "your input has numbers in it."

    valid =  False  
    while not valid:
        response = input(question)
        has_errors = ""

        # look at each character in string and if it's a number, complain
        for letter in response:
            if letter.isdigit():
                has_errors = "yes"
                break

        if response == "":
            print("Sorry, this can't be blank")
            print()
            continue
        elif has_errors != "":
            print(error)
            print()
            continue
        else:
            return response

# Main Routine goes here

for item in range(0,100):

    valid_name = not_blank("input a name which does not contain numbers ")

    print("Your input name is  {}, your input is good".format(valid_name))
    print()
