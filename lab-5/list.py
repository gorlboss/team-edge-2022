#********************************************************************
                                                                  
 #  Team Edge list Challenges!                                     
  
 #  Use this program to learn about Python lists:
    
 #  1. Declare and store data in lists
 #  2. Access list data by index
 #  3. Modify list data by index
 #  4. Multi-dimensional lists (lists inside lists!)
 #  5. List methods: append() and pop()
 #  6. The length of the list - introduce conditionals
 #  7. Strings as sequences - join() split() 
 #  
 #  Follow the -->To Dos ! run the program to test often and debug
 # ***************************************************************





print("------------------- CHALLENGE 1 -------------------")
#This is an empty Python list:
empty_list = []

#this list has 5 Strings. We can print it:
names = ["Sam", "Wolf", "Alex", "Bella", "Shaquan"]
print("names: " + str(names))  

#-->TODO: Declare another list called friends with at least 5 strings inside (if you don't have 5 friends make them up!)

friends = ["Sophia", "Destiny", "Ishika", "Zoya", "Nelson"]

#this list holds numbers
numbers = [12.9, 23.4 , 100, 3.1415 , 500, 1.20]
print("numbers: " + str(numbers)) 

#-->TODO: Declare another list and add in at least 5 numbers. Why five? I don't know. It just feels right.

numbers2 = [16.25, 23, 54.36, 69, 72.53]

#this list has mixed data types. It's allowed in Python!
random_stuff = ["Aardvark", True, False, 1.23, "Grandpa"]
print("random: " + str(random_stuff))

#-->TODO: Declare and log a list filled with the first 5 things that come into your head, booleans, Strings, numbers are all cool,

random = ["rocks", "hi!", 123.456, False, True]

#-->TODO: Declare and log two more lists with whatever you want. 

camilloLyrics = ["Seven foot frame,", "rats along his back.", "When he call your name it all fades to black.", "Yeah he reads your dreams and feasts on your screams.", "we don't talk about Bruno-no-no-no~"]
print(camilloLyrics)

doloresLyrics = ["Hey grew to live in fear of Bruno stuttering and stumbling.", "I could always hear him sort of muttering and mumbling.", "I associate him with the sound of falling sand.", "tss, tss, tss", "Such a heavy lift with a gift so humbling.", "Always left Abuela and the family fumbling.", "Grappling with prophecys they couldn't understand.", "Do you understand?"]

print("------------------- CHALLENGE 2 -------------------")
 
#This code logs the first element of the names list:
print("The first name is " + names[0])

#-->TODO: Print the name of your best friend from your friends list

print("My bestie is " + friends[1])

#-->TODO: Print the first AND last elements of any list you made, or make a brand new one.

print("My first name is " + friends[0] + " and my last name is " + friends[4] )

print("------------------- CHALLENGE 3 -------------------")
#this code changes the value of the second element of the names list, then we print the list:
names[1] = "Alyssa"
print(names)

#-->TODO: Replace your friends! Modify the list to replace any or all of your friends with new ones.

friends[3] = "Shawn"
print(friends)

#The code below uses the times_ten() function to multiply the first element in our list by 10:
def times_ten(number):
    number = number * 10
    return number

numbers[0] = times_ten(numbers[0])
print(numbers)

#-->TODO: Write another function that multiplies a number by 1000 and print the list, as above 

def times1000(number):
  number = number * 1000
  return number
numbers2[4] = times1000(numbers2[4])
print(numbers2)

#-->TODO: Replace your random list elements with anything you want, using the index. 

random[1] = "I replaced this string value"
print(random)

print("------------------- CHALLENGE 4 -------------------")

#As it turns out, you can also store lists within lists! Declare them and store them as variables.
child_list_1 = ["This", "is" , "a", "meaningless", "list"]
child_list_2 = ["This" ,"list" , "is", "also" , "meaningless"]
parent_list = [child_list_1, child_list_2]
print("This list has babies: " + str(parent_list))

#-->TODO: Store and print all the lists we have worked on thus far in a new parent list

masterOfAllLists = [friends, numbers2, random, camilloLyrics]
print(masterOfAllLists)

print("------------------- CHALLENGE 5 -------------------")

#We can add elements into a list wihtout replacing anything. Using append() adds an element to the END of the list:
movies = ["Toy Story 4", "The Dark Knight", "Parasite"]
print("Movies: " + str(movies))
movies.append("Joker")
movies.append("Black Panther")
print("Movies now has: " + str(movies))

#-->TODO: Declare a list with 5 favorite songs

faveSongs = ["Jesus in LA Alec Benjamin", "Brighter Days Jomie", "Popular Girl, Typical Boy Powfu", "Fire Drill Melanie Martinez", "911 Elise"]

#-->TODO: Add 2-3 more songs using .append() and print both before and after.

print(faveSongs)
faveSongs.append("im used to it Powfu")
faveSongs.append("prom dress mxmtoon")
faveSongs.append("100 Bad Days AJR")
print("My new favorite songs are" + str(faveSongs))

#We can also remove elements using .pop(), which removes the last element or the element at the given index. You can store it after it comes out:
cities = ["New York", "Oakland", "Las Vegas", "Topeka"]
print("cities: " + str(cities))
unwanted_city = cities.pop()
print("unwanted city: " + str(unwanted_city))

#-->TODO: remove your last song using .pop() and print the removed element as above

removedSong = faveSongs.pop()
print(removedSong + " is no longer one of my favorite songs")

#Note: there are more methods to remove and modify list elements. We will cover those later

print("------------------- CHALLENGE 6 -------------------")

#Lists have properties. one of the most important is the size, or length. Here are two examples:
print(f"I have {len(names)} friends")

how_many_cities = len(cities)
print(f"There are {how_many_cities} ciites in my list")

#-->TODO: Print out the number of friends, or other items from other lists using string literals as above

print(f"I have {len(friends)} friends")

#The len() function is key, especially in conditionals or to simply count how many times to do something.

if len(numbers) > 3:
    print("There are more than 3 numbers in my list")
else:
    print("I need more numbers in my list!!!")

#-->TODO: Write another if/else statement to check the size of your songs list. If you have 5 of less, add two more songs!

if len(faveSongs) <= 5:
  print("Add some more songs to your list ;)")
else:
  print("You cool fam")

print("------------------- CHALLENGE 6 -------------------")

#Strings can also be thought of lists:
sentence = "I am a boring sentence."
boring_list = sentence.split(" ") #split the sentence by each space to get a list of words
print("boring sentence as a list: " + str(boring_list))

word = "Abracadabra"
word_split_list = word.split() #split by nothing, and you get each character in the string as its own element.
print("letter by letter: " + str(word_split_list))

#using this you can split strings up by any character!

#-->TODO: Change the name of the person who is late in this sentence and print it.
split_me = "I heard Alex was late to class today."
listed_split_me = split_me.split(" ")
listed_split_me[2] = "Sophia"
print(listed_split_me)

#-->TODO: Add an exclamation mark to this sentence using split() and append(), then print. (yes, there are other ways, but...)
make_me_exciting = "What a wonderful day"
exciting_list = make_me_exciting.split(" ")
exciting_list.append("!")
print(exciting_list)

#We can also join our list elements into a string using.....join()!
rejoined = " ".join(boring_list)  #joins it using spaces
print('back in one piece: ' + rejoined)

#-->TODO:  Finally, put the split_me sentence today and the make_me_exciting strings back together and print. You should see a string

rejoined_split = " ".join(listed_split_me)
print(rejoined_split)

rejoined_excitment = " ".join(exciting_list)
print(rejoined_excitment)