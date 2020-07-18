  
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

# Checks answer to y / n question is yes / no
def yes_no(question):

  to_check = ["yes", "no"]
  
  valid = False
  while not valid:

    response = input(question)
    print(response)

    for item in to_check:
      if response.lower() == item:
        return response
      elif response.lower() == item[0]:
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
def not_blank (question):
    error = "your recipe name has numbers in it."

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
  print("Please enter the ingredients for {}".format(title))

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
      item_amount = num_check(int, "What is the amount of the ingredients? ", 0)
      item_amount_unit = g_kg("What is the unit of the amount ? (g or kg) ")
      item_price = num_check(float, "What is the listing price of the ingredient ({})? ".format(item_name), 0)
      item_weight = num_check(int, "What is the weight of the listing ingredients? ", 0) #add
      item_weight_unit = g_kg("What is the price unit? (g or kg) ")
      #item_unit_price=float(item_price/item_weight)

    else:
      break

    # Add name and cost for each item to 'row' list
    ingredients.append(item_name)
    ingredients.append(int(item_amount))
    ingredients.append(item_amount_unit)
    ingredients.append(float(item_price))
    ingredients.append(int(item_weight))
    ingredients.append(item_weight_unit)
    #ingredients.append(float(item_unit_price))
    
    # Add each row to the master list
    all_ingredients.append(ingredients)

  return all_ingredients


# Main

# Title / Welcome
print("")
print("****** Welcome to the Recipe Calculator ******")

# Ask user if its their first time and if it is, display instructions
instructions()

print("")

recipe_name = not_blank("What is the name of the recipe? ")   # check not blank

print("Recipe: " + recipe_name)

print("")

servings_factor = num_check(float, "How many servings will you make? ",0)  # check that this is an integer more than 1

print("Servings: {:.2f}".format(servings_factor))

print("")

all_ingredients = get_ingredients(recipe_name)


print()
print("********* Recipe Name and servings ***********")
print()
print("Recipe Name: " + recipe_name)
print("Servings: {}".format(servings_factor))

print()
print("********* Ingredient cost ***********")
print()
#print("Name Weight price cost")
total_cost = 0
servings = 0
print(all_ingredients)

for ingredient in all_ingredients:
  #print("Ingredient : {} ".format(ingredient))
  cost = 0
  unit_cost = 0.0
  # unit price unit $/kg
  if ingredient[5] == 'kg':
    unit_cost = ingredient[3]/ingredient[4]
  else: 
    unit_cost = ingredient[3]*1000/ingredient[4]
  
  if ingredient[2] == 'kg':
    cost = ingredient[1]*unit_cost
  else:
    cost = ingredient[1]/1000*unit_cost

  total_cost += cost 
  
  print("Item:{} Amount:{}{} Price:${}/{}{} Cost: ${:.2f}".format(ingredient[0],ingredient[1],ingredient[2],ingredient[3],ingredient[4],ingredient[5], cost))
  
print()
print("********* Total cost ans per serve ***********")
print()
servings = total_cost/(float)(servings_factor)

print("Total cost: ${:.2f}".format(total_cost))

print("Per Serve: ${:.2f}".format(servings))

