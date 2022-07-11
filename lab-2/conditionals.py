# -------------------------------------------- 
# Day 2 Challenges
# -------------------------------------------- 

message = "Welcome to Day 2!\nToday we are learning about conditionals.\nLet's practice writing some conditionals of our own!\n"
print(message)
# -------------------------------------------- 

print("------------------- Challenge 1 -------------------")
# Can you drive?
   # Prompt the user to enter their age.
   # Write conditional statements that print out whether you can drive in your city. 

age = input("\nCan you drive? Enter your age:")
print(" ")
if age < "70" and age >= "16":
  print("You can drive, enjoy!\n")
elif age >= "70":
  print("You are no longer able to drive, sorry!\n")
elif age < "16":
    print("You can't drive, get off the road.\n")
  
# -------------------------------------------- 

print("------------------- Challenge 2 -------------------") 

# Who placed first?
   # Write conditional statements that checks which is the highest and prints the highest score. 
   # Hint: Create three variables and assign them random scores. 

score1 = 481
score2 = 652
score3 = 973

highestScore = score1
print("Highest score is: ", highestScore)

if score2 > highestScore:
  highestScore = score2
  print("Higest score is: ", highestScore)
  if score3 > highestScore:
      highestScore = score3
      print("Highest score is: ", highestScore)
  
# -------------------------------------------- 

print("------------------- Challenge 3 -------------------")

# One of the most common parts of our daily routine is checking the weather. 
# Our outfit and accessories are dependent on the temperature and conditions outside. 
# ie. We're probably not going to wear shorts out when it's snowing...


# **** Challenge 3: Part 1 ****
# Write a conditional statement that checks the value of the weather variable 
# and prints out a weather report based on the current weather:
# Rainy: Bring an umbrella
# Sunny: Wear a hat and sunglasses
# Snowing: Wear gloves and a scarf 

# Here's a variable to get you started:
weather = "snowing"

if weather == "rainy":
  print("It's raining!\nMake sure to bring an umbrella today!\n")
elif weather == "sunny":
  print("It's sunny out.\nYou should wear a hat and some sunglasses.\n")
elif weather == "snowing":
  print("It's snowing!\nGo get your gloves and scarf and enjoy the snow!\n")

# Tip: Try changing the value of the weather variable to test your other conditions.

# **** Challenge 3: Part 2 ****
# Now that you've written conditions for specific weather forecasts, let's also add in temperature! 
# You can't dress accordingly if you only know that it's raining outside but not how cold it is!
# For example:
    # If it's raining and 60 degrees, you might want to bring your umbrella and wear a light jacket.
    # However, if it's raining and 30 degrees, you might want to break out a warmer jacket with your umbrella instead. 
    
   # Add to your conditional statements above and modify your weather reports to also take into account the temperature. 
   # Make sure to account for at least three different temperatures!
   # Hint: You will need another variable to keep track of the temperature.

weather = "snowing"
temp = 28

if weather == "rainy":
  print("It's raining!\nMake sure to bring an umbrella today!")
  if temp <= 65 and temp > 50:
    print("Maybe bring a light jacket as well.\n")
  elif temp < 50:
    print("Bring a thick jacket as well.\n")
elif weather == "sunny":
  print("It's sunny out.\nYou should wear a hat and some sunglasses.")
  if temp >= 70 and temp < 80:
    print("Wear some shorts too!\n")
  elif  temp > 80:
    print("It's real hot out here. Make sure to drink water!\n")
elif weather == "snowing":
  print("It's snowing!\nGo get your gloves and scarf!")
  if temp <= 50 and temp > 30:
    print("It's really cold too. Don't forget a thick jacket!\n")
  elif temp < 30:
    print("It's way too cold, you should just stay inside.\n")

# -------------------------------------------- 

print("------------------- Challenge 4 -------------------")

# Prompt the user to enter the day of the week (1-7 representing Monday - Sunday)
    # Write a set of conditionals that will take a number from 1 to 7 
    # and print out the corresponding day of the week. 
    # Make sure to add a statement that accounts of any numbers out of range! */

day = input("\nPlease give a number 1-7 indicating the day of the week:")
if day == "1":
  print("\nToday is Sunday\n")
elif day == "2":
  print("\nToday is Monday\n")
elif day == "3":
  print("\nToday is Tuesday\n")
elif day == "4":
  print("\nToday is Wednesday\n")
elif day == "5":
  print("\nToday is Thursday\n")
elif day == "6":
  print("\nToday is Friday\n")
elif day == "7":
  print("\nToday is Saturday\n")
else:
  print("\nEntered number invalid\n")

# -------------------------------------------- 

print("------------------- Challenge 5 -------------------")

# A leap year is a calendar year that contains an additional day added 
   # to keep the calendar year synchronized with the astronomical year or seasonal year.
   # To calculate if a specific year is/was a leap year, you can follow the following steps:
     # 1. If the year is evenly divisible by 4, go to step 2. Otherwise, go to step 5.
     # 2. If the year is evenly divisible by 100, go to step 3. Otherwise, go to step 4.
     # 3. If the year is evenly divisible by 400, go to step 4. Otherwise, go to step 5.
     # 4. The year is a leap year (it has 366 days).
     # 5. The year is not a leap year (it has 365 days).

  # Those are a lot of conditions...

  # Your challenge is to translate the steps above into conditionals which will evaluate if the 
  # year stored in a variable is/was a leap year.

year = 2012

if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print("\nThis year is a leap year! (It has 366 days)\n")
  else:
    print("\nThis year is a leap year! (It has 366 days)\n")
else:
  print("\nThis year is NOT a leap year! (It has 365 days)\n")