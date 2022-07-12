#********************************************************************
 #                                                                  
 #  Team Edge List Mini-project: FOR LOOP CHALLENGES
 # 
 #   Complete the following loop challenges below. Follow the ToDos
 #   1. COUNTER: Write a loop that prints a happy birthday message for every
 #      year you have been alive.
 #   2. ITERATOR: Write a for for loop that prints every item in a list

 #   3. EVEN COUNTDOWN: Write a for loop that counts down from 100 to 0, 
 #      printing only the odd numers
 #   4. FINDER: Write a function that takes in a list and a word and prints 
 #      CONGRATULATIONS!! if the word is found in the list
 #   5. NESTED: Write a function that logs every letter in a sentence
 # 
 # ***************************************************************/
import random

print("------------------- CHALLENGE 1 : COUNTER -------------------")

#this list prints every number between 0 and 10, using range

for x in range(11):
    print(f"Counter at: {x}")
   

#-->TODO: Write a loop that prints a happy birthday message for every year you have been alive.

for x in range(1,15):
  print(f"\nHappy {x}th Birthday")
  
print("------------------- CHALLENGE 2 : ITERATOR ----------------------")

#here is a list full of colors...
colors = ['red' , 'violet' , 'cyan' , 'pink' , 'lime' , 'white' , 'yellow', 'black' , 'magenta', 'green', 'orange']

#This is how you can iterate through a list:
for x in colors:
    print("The color is: " + x)

#-->TODO: Declare a list with at least 10 animals. You provide the animals.
animals = ["Rhino", "Sloth", "Koala", "Bear", "Bee", "Bunny", "Duck", "Dragon", "Salamander", "Cat"]

#-->TODO: Print all the animals in the array with a for loop. 

for x in animals:
  print("\n" + x)
  
print("------------------- CHALLENGE 3 : EVEN COUNTDOWN ------------------")


#This makes a random number between 0-50
random = random.randint(0, 50)

#this if/else statement checks if the number is even using the modulo operator (%)
if random % 2 == 0:
    print(str(random) + " is even!")
else:
    print(str(random) + " is odd!")

#-->TODO: Write a function that counts BACKWARDS from 100 and prints only odd numbers

def oddNumbs():
   for x in range(99,0,-2):
     print(x)
oddNumbs()
print(" ")

#-->TODO: Write a function that counts BACKWARDS from the given random number and prints only even numbers

def evenNumbs():
  if random % 2 == 0:
    for x in range(random,0,-2):
      print(x)
evenNumbs()
print(" ")

print("------------------- CHALLENGE 4 : Finder ------------------")

#This code uses the in operator to see if an element exists in a list. It only has to appear once.
color = input('Type a one word color and see if it is one of my favorite colors! >> ')
if color in colors:
    print("Yes, that color is a fav")
else:
    print("No, that color is not one my favorites")

#-->TODO Declare a list of any strings you  want: cities, friends, movies, etc.

theThings = ["Encanto", "Philly", "Channing Tatum", "Detroit", "Destiny", "Mom", "Bruno", "Melanie", "Sociopath"]

#-->TODO Prompt the user to "Guess" if an element is present. Store their response in a variable

#guess = input("Guess what I am thinking off! >>")

#-->TODO Write function to prompt the user and see if the element is present. If so, print CONGRATULATIONS!

def mindReader():
  guess = input("Guess what I am thinking off! >>")
  if guess in theThings:
    print("Wow you read my mind!")
  else:
    print("Sorry that's not it~")
 
#-->TODO Call your function.

mindReader()

print("------------------- CHALLENGE 5 : Nested ------------------")

#this is how you get the length of a word:
big_word = "antidisestablishmentarianism"
print(f"{big_word} has {len(big_word)} letters")

#this is how you can nest for loops, one insde the other! These loop through all the colors, and then through all the characters in the color
for color in colors:
#for all the colors:
    print(color)
    for c in color:
        print(" - " + c) #log each letter. Remember, a string is also an array of characters.


#-->TODO Write a function that prints every letter in a sentence that a user enters.
def sentenceBreaker():
  breakup = input("Enter a sentence (plz don't make it too long) >>")
  print(breakup)
  for b in breakup:
        print(" - " + b)
sentenceBreaker()
#-->CHALLENGE: Let the user know which word is the shortest one!
