  
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
      response = float(input(question))

      if response > lowest:
        return response
      else:
        print(error)

    except ValueError:
      print(error)

# Checks answer to y / n question is yes / no
def yes_no(question):

  to_check = ["yes", "no"]
  
  valid = False
  while not valid:

    response = input(question)
    print(response)

    for item in to_check:
      if response == item:
        return response
      elif response == item[0]:
        return item

    print("Please enter either yes or no...\n")

# Checks answer to y / n question is g / kg
def g_kg(question):

  to_check = ["g", "kg"]
  
  valid = False
  while not valid:

    response = input(question)

    for item in to_check:
      if response == item:
        return response
      elif response == item[0]:
        return item

    print("Please enter either g or kg...\n")

# Checks a response to a question is not blank
def not_blank(question):

  valid = False
  while not valid:
    response = input(question)

    if response != "":
      return response
    else:
      print("Sorry, this can't be blank.\n")

# Displays instructions if program has not been used before
def instructions():
  
  first_time = yes_no("\nIt this your first time using the program? ")

  # instructions only display if user says it is their first time using the program
  if first_time == "no":
    return ""
  
  print("")
  print("***** Instructions ******")
  print("")
  print("This program will ask you for...")
  print("- The name of the recipe")
  print("- How many ingredients of the recipe")
  print("- The costs for each component of the product")
  print("")
  print("It will then output an itemised list of the costs with subtotals for the variable and fixed costs.")
  print("Finally it will tell you how much you of the cost and cost per serving")
  print("")

# Asks user for item and cost and returns 2D list
def get_ingredients(title):

  # Set up master list to hold all costs
  all_ingredients = []  
  print()
  print("Please enter the {}".format(title))

  valid = False
  while not valid:
    # List to contain each item (name, amount)
    ingredients = []

    if len(all_ingredients) == 0:
      comp_question = "Ingredients Name: "
    else:
      comp_question = "Ingredients name (or 'xxx' to move on): "

    item_name = not_blank(comp_question) 

    if item_name.lower() == "xxx" and len(all_ingredients) == 0:
      print("You must have at least one ingredients!!!!")
      continue

    if item_name.lower() != "xxx":
      item_amount = num_check(float, "What is the amount of the ingredients? ", 0)
      item_unit = g_kg("What is the unit of the amount ? (g or kg) ")
      item_price = num_check(float, "What is the price of the ingredient ({})? ".format(item_name), 0)
      item_price_unit = g_kg("What is the price unit? (g or kg) ")

    else:
      break

    # Add name and cost for each item to 'row' list
    ingredients.append(item_name)
    ingredients.append(float(item_amount))
    ingredients.append(item_unit)
    ingredients.append(float(item_price))
    ingredients.append(item_price_unit)
    
    # Add each row to the master list
    all_ingredients.append(ingredients)

  return all_ingredients


# Main

# Title / Welcome
print("****** Welcome to the Recipe Calculator ******")

# Ask user if its their first time and if it is, display instructions
instructions()

print("")

recipe_name = not_blank("What is the name of the recipe? ")   # check not blank

print("Recipe: " + recipe_name)

print("")

servings_factor = num_check(float, "How many servings will you make? ",0)  # check that this is an integer more than 1

print("Servings: {}".format(servings_factor))

print("")

all_ingredients = get_ingredients(recipe_name)

print("Ingredients List:")

total_cost = 0
servings = 0

for ingredient in all_ingredients:
  print("Ingredient : {} ".format(ingredient))
  cost = 0
  unit_price = 0
  # unit price unit $/kg
  if ingredient[4] == 'kg':
    unit_price = ingredient[3]
  else: 
    unit_price = ingredient[3]*1000
  
  if ingredient[2] == 'kg':
    cost = ingredient[1]*unit_price
  else:
    cost = ingredient[1]/1000*unit_price

  total_cost += cost 
  
  print("Ingredient price : {} Cost: ${}".format(ingredient[0], cost))

servings = total_cost/(float)(servings_factor)

print("Total cost: {}".format(total_cost))

print("Per Serve: {}".format(servings))

