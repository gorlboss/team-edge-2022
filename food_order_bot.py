# -------------------------------------------- 

	# You've just learned about variables, conditionals, functions, and user input. 
	# You've also created a basic calculator in a previous project.
	
	# Now imagine you are going out to eat with two other friends.
	# Are you at a restaurant for a meal? Are you grabbing boba? Or are you just going to an ice cream parlor?
	# At the end of the meal, you and your friends have to split the bill. 

	# Wouldn't it be great if we could automate that math?

					# Let's try it!

# -------------------------------------------- 

# Scenario Parameters: 

	# When you and your friends eat out, each of you have the option to order one or multiple items.
	# What kind of items are available to order?

	# At the end of the order, the receipt comes and you all have to calculate the cost for each person:
	# Don't forget the tax and tip!

# After this program finishes running, it should output a specific total for each person

# -------------------------------------------- 


# -------------------------------------------- 

# Part 1:
# Let's start by asking taking the order of the group(you and two friends). What did each person order?

# Write a function that will take the group's order:
# - Prompt the user to enter the price of each item they ordered
# - Return the cost 

# Remember! Functions are meant to be reusable, so write a function that will work when called for each person!

# --------------------------------------------

# def itemsCost():
#   name = input("What is your name?: ")
#   drinkCost = input(f"How much is your drink {name}?:$ ")
#   mealCost = input(f"How much is your meal {name}?:$ ")
#   return name, round(float(drinkCost),2), round(float(mealCost),2)
   
# name1, drink1, food1 = itemsCost()
# print(" ")
# name2, drink2, food2 = itemsCost()
# print(" ")
# name3, drink3, food3 = itemsCost()
# print(" ")

# -------------------------------------------- 

# Part 2:
# Now that you have the costs of everything ordered, let's calculate the cost of each person's order(including tip and tax).

# Write a function that will calculate the cost of each person's order, including:
# - Cost of all of their ordered items
# - Tax (Look up the sales tax of your city)
# - Tip (Give the user the option to enter how much they want to tip)

# Remember! Functions are meant to be reusable, so write a function that will work when called for each person!

# -------------------------------------------- 

# def orderCost(name, drink, food):
#   tip = input(f"How much would you like to tip {name}:$ ")
#   total = drink + food
#   tax = total * float(0.1045)
#   totalReceipt = total + tax + float(tip)
#   return round(totalReceipt,2)

# receipt1 = orderCost(name1, drink1, food1)
# print(" ")
# receipt2 = orderCost(name2, drink2, food2)
# print(" ")
# receipt3 = orderCost(name3, drink3, food3)
# print(" ")

# -------------------------------------------- 

# Part 3:
# Let's print out a receipt for each person.

# Write a function that will take the values of each person's order and total cost and print it out in an appealing way.

# The receipt should include:
# - Cost of each item
# - Total cost for each person

# Remember! Functions are meant to be reusable, so write a function that will work when called for each person!

# -------------------------------------------- 

# def receipt(name, drink, food, receipt):
#   print(f"{name} you ordered a drink for ${drink}.\n Food for ${food}.\n Your meal total,including tax and tip, is {receipt}!\n")

# total1 = receipt(name1, drink1, food1, receipt1)
# total2 = receipt(name2, drink2, food2, receipt2)
# total3 = receipt(name3, drink3, food3, receipt3)



# -------------------------------------------- 

# Part 4: Upchallenges!

# How many of these upchallenges can you implement?

# - Make sure the user is only entering numbers. If they enter an invalid value, prompt them to re-enter. 
# - The displayed prices should only have two decimal places.[Done!]
# - Can you adjust your program to account for any shared items ordered for the group?
# - Display the tax and tip values
# - Implement a rewards system (stamp cards, buy one get one, etc)
# --------------------------------------------

def getItemForPerson(name):
  item = input(f"What would you like to order {name}?: ")
  cost = input(f"How much does this {item} cost?: $")
  return item, float(cost)

def calculateTotal(cost):
  tip = input("How much would you like to tip?: $")
  tax = cost * float(0.1025)
  total = cost + tax + float(tip)
  return round(total, 2)

def printReceipt(name, item, cost, total):
  print(f"{name} you ordered {item} for ${cost}. Your total, with tax and tip included, is ${total}")
  
def getOrder():
  name = input("What is your name?: ")
  item, cost = getItemForPerson(name)
  total = calculateTotal(cost)
  printReceipt(name, item, cost, total)

getOrder()
getOrder()
