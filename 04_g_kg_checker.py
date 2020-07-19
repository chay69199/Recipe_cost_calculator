  
import math



# Checks unit is g or kg
def g_kg(question):

  to_check = ["g", "kg"]
  
  valid = False
  while not valid:

    response = input(question)

    for item in to_check:
      if response.lower() == item:
        return response.lower()

    print("Please enter either g or kg...\n")

# Loops to make testing faster...
for item in range(0,100):
  Test = g_kg("Please input ")
  print("You said '{}'\n".format(Test))
