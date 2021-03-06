  
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

# Displays instructions if program has not been used before
def instructions():
  
  first_time = yes_no("\nIs this your first time using the program? ")

  # instructions only display if user says it is their first time using the program
  if first_time == "no":
    return ""
  
  print("")
  print("********** Instructions **********")
  print("")
  print("This Recipe Cost Calculator program will ask you for:")
  print("- Recipe name and serving size.")
  print("- List each ingredient in the recipe.")
  print("- List the amount of the ingredient needed.")
  print("- List the cost of each ingredient.")
  print("")
  print("The program will work out the totoal cost for the recipe and cost per serving")
  print("")


#main
for item in range(0,100):
    instructions()


