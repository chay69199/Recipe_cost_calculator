  
import math


# Checks answer to y / n question is yes / no
def yes_no(question):

  to_check = ["yes", "no"]
  
  valid = False
  while not valid:

    response = input(question)
    print(response)

    for item in to_check:
      if response.lower() == item:
        return response.lower()
      elif response.lower() == item[0]:
        return item

    print("Please enter either yes or no...\n")


# Loops to make testing faster...
for item in range(0,100):
  Test = yes_no("Please input ")
  print("You said '{}'\n".format(Test))
