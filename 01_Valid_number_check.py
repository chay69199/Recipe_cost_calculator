  
import math

# Checks response is a valid number
def num_check(type, question, lowest):

  # Set up error message so that it specifies either 'an integer' or 'a number' depending on the 'type'.
  if type == int:
    error_specific = "an integer"
  else:
    error_specific = "a number"

  error = "Please enter {} that is more than {} \n".format(error_specific, lowest)

  valid = False
  while not valid:

    # Ask the question and check that the answer is valid
    try:
      response = type(input(question))

      if response > lowest:
        return response
      else:
        print(error)

    except ValueError:
      print(error)


# **** Main Routine Goes Here

# Test int
Test_int = num_check(int, "input an int? ", 0)

# Test number
Test_number = num_check(float, "input an number", 0)

print("The input int is {} The input number is {:.2f}, your input is good".format(Test_int, Test_number))
