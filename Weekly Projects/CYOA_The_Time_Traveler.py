######CLASSES######
class Person:
  def __init__(self, name=None, lang=None, descr=None, inventory=[]):
    self.name = name
    self.descr = descr
    self.inventory = inventory
    self.response = ""       

class Room:
  def __init__(self, descr=None, people=[], name=None):
    self.descr = descr
    self.people = people
    self.name = name

  def enter(self, person):
    print(f"You enter the {self.name}. {self.descr}\n")
    for num in range(len(self.people)):
      print(f"{num}: {self.people[num].descr}")
    self.people.append(person)
    selection = input("\nWho do you wish to talk to? (pick a number): ")
    return self.people[int(selection)]
    
####### SETUP CODE #######

womanInRed = Person()
womanInRed.name = "Ravena"
womanInRed.descr = "In the corner you notice a woman. She wears a bright red clock. She seems to be staring directly at you."

bartender = Person()
bartender.name = "Bartender"
bartender.descr = "You look towards the bar. The bartender seems to be busy with customers."
bartender.response = "He says some word that you don't understand and points towards the woman in the corner.\n"

player = Person()
player.inventory = []

tavern = Room()
tavern.descr = "A large room, filled with chatting customers. Something about it feels dangerous..."
tavern.people = [womanInRed, bartender]
tavern.name = "Tavern"

blacksmith = Person()
blacksmith.name = "Kiyana"
blacksmith.descr = "There is a sound of metal clanging somewhere deep inside the workshop. You follow the sound until you reach a woman. Her bronze skin glistens with sweat, muscles rippling as she raises her hammer and strikes the metal. Scars criss cross all up and down her arms."

workshop = Room()
workshop.name = "workshop"
workshop.descr = "The space looked small on the outside. But the inside is of unparalleled size. Books are stacked to the floor. As you move through the shop you see even more rooms, with different tools and creations."
workshop.people = [blacksmith]

##################################TODO LIST###################################
  #Fix my if statments so that it'll re-promtp 
  #when given an invalid answer (check phone notes)

  #Add a sleep function in between function calls/print statment chunks so that it's less jarring
##############################################################################

###### Functions ######
import random
from time import sleep

restTime = 3

def printQuestions(questions):
  for num in range(len(questions)):
    print(f"{num}: {questions[num]}")

def answerQuestions():
  # Goal: Print the dialogue. Allow a user to select from a bank for questions.
  questions = ["How do you know that I'm the chosen one?", "What’s the machine?", "Can you time travel too?", "Are there more of you?", "Are there more people who are looking for me?", "How did I get here? I was sleep in my bed last I remember", "Why did we have to leave the tavern", "What happened to my old clothes?"]
  answers = ["The glasses told me", "It’s what the first traveler used; it's the only way we can get back to our timelines.", "Sure I can, that's how I found you. We copied the tech in the original machine and miniaturized it. She holds up her wrist to show her watch. It’s just that we can’t get back to where we were because... She pauses. Anyways we have to fix the Machine", "Yeah, lots of us got sucked in by the experiment. We’ve been stuck for ages. Some of us have been trying to look for you, others have been just wreaking havoc. Some just try to settle down someplace quiet.", "Yeah...they're...y'know around...they just missed you I guess. How unlucky for them...", "Oh...uh...I don't really know. I knew you would be here though...the glasses told me that much. You...must have traveled here yourself...on accident or something.", "Someone tipped them off. Your face has been on wanted posters all morning. If they had seen you, instead of a peacful walk out, we would have had to run for our lives. Aldosans are known for being violent.", "The glassses made some new ones for you so that you cna fit in with the times."]    

  # While there are items in the questions list:
  while len(questions) > 0:
    # Print the questions 
    printQuestions(questions)
    print(" ")
    # Get the selection. 
    questionNum = input("Enter the number for the question you wish to ask: ")
    # Convert the selection from a string to an integer
    questionNum = int(questionNum)
    # Check that the question number is allowed
    if 0 <= questionNum <= len(questions):
      # Print the response for the selection
      print(f"\nThe woman replies: {answers[questionNum]}\n")
      # Remove the selection from the questions list
      questions.pop(questionNum)
      answers.pop(questionNum)
      sleep(restTime)
    else:
      print("\nThis answer is not an option, please re-enter.\n")

def answerQuestions2():
  # Goal: Print the dialogue. Allow a user to select from a bank for questions.
  questions = ["What are you doing with my glasses?", "Do...do you know a woman who wears a red cloak", "What do the shards do?", "What exactly are shards?", "Why are the glasses the only way to find the shards?", "If the shards hold energy, and time traveling take up a lot of energy, how am I able to travel around so easily?", "Did you make this place?", "What were you working on earlier?"]
  answers = ["I'm fixing them. They are broken if you hadn't noticed. They are supposed to help you find the shards but they're all jacked up. If you try following these things now. They'd probably lead you to your death.", "Woman with a red cloak? Ravena...huh, haven't heard of her in a while. She must be back.", "They are the only thing that can fix the machine, but they are also the keys to the other shards. The glasses interact with them. Everytime the glasses sense a shard nearby it'll tell you and do it's best to get you there.", "They are little crystals that hold energy. There were more but most were destroyed with the original jump. So these are the last few. Without them we'll never get home.", "A long time ago, someone decided to that they liked jumping around through time and space. So they hid the crystals and used the glasses to keep them hidden. Then the idiot went and erased their memory so no one could get the information except for the chosen one.", "That one I don't know. Those glasses were especially made by the person who got us all stuck here. My best guess is that they must have made some seperate energy source for you.", "Yeah I did. I was head engineer of the team that originaly made the machine. I built this place to help the occasional traveler that passes through.", "Oh, that, I was just working on a dagger. This world has magic so I was just infusing it with some magic. It was supposed to be for a client but they bailed. I'm just having fun working on it."]    

  # While there are items in the questions list:
  while len(questions) > 0:
    # Print the questions 
    printQuestions(questions)
    print(" ")
    # Get the selection. 
    questionNum = input("Enter the number for the question you wish to ask: ")
    # Convert the selection from a string to an integer
    questionNum = int(questionNum)
    # Check that the question number is allowed
    if 0 <= questionNum <= len(questions):
      # Print the response for the selection
      print(f"\nKiyana replies: {answers[questionNum]}\n")
      # Remove the selection from the questions list
      questions.pop(questionNum)
      answers.pop(questionNum)
      sleep(restTime)
    else:
      print("\nThis answer is not an option, please re-enter.")
      
    
  
def timeTravel():
  print("A rift opens in front of you. You step through. Before you now lay two paths. One to the left and one two the right.\n")
  while True:
    path = input("Do you wanna go left or right?: ")
    if path == "right":
      break
      global gameIsOn
      gameIsOn = False
      print("You go through the portal on your right. You end up in a dark room. The portal closes behind you. You are now trapped.\nGAME OVER")
    elif path == "left":
      print("\nYou go through the portal on the left.")
      break
    else:
      print("\nAnswer invalid, please re-enter.\n")
  #TODO Fix if statement so that if you enter an invalid entry it re-prompts

def printList(puzzles):
  for x in range(len(puzzles)):
    print(f"{x}: {puzzles[x]}")
def tileRoom():
  while True:
    global gameIsOn
    #If the first letter is capitalized that the hint. If not then it's a throw off
    signHint = ["Up the window Rolled the Dog.\nLaughing at the Diasy who dareD to RiDe aLong.\nRainbows fLurried through the air.\nlaughteR\nlaughteR\nEveRywheRe", "Up the meadows\nUnder the moon\nUntiL the Lanes Dried up the Lagoons\nFReedom rains\nUnUnified", "down the Road\nThe Unicorn flies\nRaceing the towaRDs the Red sky.\n Ugly LLamas stop to stare\nUgly chiLDRen eveRywheRe", "rings wiLL rUn UnDer the Rushing Dam\nwraiths will RoLL from the UnDeRbeLLy\nUnusuaL Urges wiLL Rise fRom the monsteR within"]
    boobyList = ["A metal spike shoots up from the tile implaing you", "Spike drop from overhead, implaing and cruching you simulateously", "A large boulder drops down crushing you", "The tile dissapears and you fall into a vat of acid", "Axes swing out from the walls, slicing you in half", "Arrows shoot out from the walls, impaing you in many places", "Fire shoot out from the wall burning you to a crisp"]
    correctSequence = ["u","r","d","l","d", "r","r", "u", "u", "u", "l", "d", "l", "u", "r", "u", "r", "r", "u", "l", "u", "u", "r", "d", "r", "u", "u", "u" ]

    print(f"You turn back towards the grid. You notice another smaller sign sitting near the edge of the grid.\nIt reads:\n\"{signHint[0]}\"\n")
  
    for x in range(len(correctSequence)):
      print("**u for up, d for down, r for right, and l for left**")
      step = input("Which way to you want to move?: ")
      if step == correctSequence[x]:
        print("\nYou step onto the tile. Nothing happens.\n")
        if x == 6:
          print(f"A sign sits at the edge of the tile. It reads:\n\"{signHint[1]}\"\n")
        elif x == 13:
          print(f"A sign sits at the edge of the tile. It reads:\n\"{signHint[2]}\"\n")
        elif x == 20:
          print(f"A sign sits at the edge of the tile. It reads:\n\"{signHint[3]}\"\n")
      else:
        #TODO make it so that the game doesn't end each time instead it just re runs the function
        print(f"You step on the tile. {boobyList[random.randint(0, len(boobyList))]}.\nGAME OVER")
        cont = input("Do you want to continue? (y/n) : ")
        if cont == "n":
          break
          gameIsOn = False
        elif cont == "y":
          print("Starting challenge again...")

  if gameIsOn != False:
    print("You step off the final tile. Directly in front of you is a wall of vines. They seem to be moving. A sign appears at your feet:\n\"Well looks like you made it after all chosen one.\nGood for you!\nBut now that your here you're probably wondering where the shard is?\nWell look closer at those vines in front of you.\"\nYou look up and notice a flash of light behind the vines. You sigh. Of course this isn't gonna be easy. You continue reading\n\"Yup, it's behind those vines. And they're not just any type of vines they are Yium vines. They don't take lightly to being cut.\nHave fun~\"n")

def challenge():
  global gameIsOn
  print("There is a large floor covered in tiles in front of you. A sign sits on you right.\n")
  reading = input("Do you want to read the sign? (y/n): ")
  if reading == "y":
    print("You turn to read the sign. It's in a different language but the glasses translate it for you.\nThe sign reads:\n\"Welcome chosen one!\nAs you can see the floor before you is covered in tiles. Each some of those tiles activate booby traps, others don't. You have to pick the right path through the tiles or else...well you know.\nGood luck~!\"\n")
    tileRoom()
  elif reading == "n":
    print("\nToo bad you're reading the sign anyways.")
    print("\nIt's in a different language but the glasses translate it for you.\nThe sign reads: \"Welcome chosen one!\nAs you can see the floor before you is covered in tiles. Each some of those tiles activate booby traps, others don't. You have to pick the right path through the tiles or else...well you know.\n Good luck~!\"\n")
    tileRoom()

  print("You look at the vines. A message pops up on the glasses:\n\"Plant Name: Ilex erythrosora \nPlant Description: Ilex erythrosora, also known as Yium vines, are found on the planet Stheno. They are carnivorous plants. They use their long thorns to trap their food and hold them until they either bleed out or die. Their epidermis is think and highly cut resistant.\nIt seems that these plants have been enhanced using magic. Their agrassiveness and cut resistance has increased.\"\n You remeber the dagger that Kiyana gave you.")
  useDagger = input("Do you want to use the dagger? (y/n): ")

  if useDagger == "y":
    print("You take the dagger out. It shines faintly with magic.\nAnother message appears fomr the glasses: \"Dirhram Dagger: Dirhram is a material that is very stong and sturdy. This dagger has also be infused with other magical properties. The slash strength and durability of this item are far higher than seen before.\" You grins and slash at the vines. The kinfe cuts through. You hear a slight sizzling sound but the knife seems to take no damage. You continue cutting through the vines.\n")
    print("You finish cutting through the vines. A horrible burning smell fills the room. You quickly cover your nose with your clothes.\nThe knife disentigrates away in your hand. You spot the shard. There is a sign at the base but you don't stop to read it. You grab the shard.")
    player.inventory.remove("Magic Dagger")
  elif useDagger == "n":
    print("You decide to save the dagger incase it can be used for later. But now you need something to cut the vines. You spot a sharp rock on the floor. You look back at the grid. One of those booby traps has to have something sharp you can use.")
    useItem = input("Do you want to use the rock or the trap?: ")
    if useItem == "rock":
      gameIsOn == False
      print("You pick the rock up off the floor and slash at the rock. Nothing happens. The vines reach out a grab you. Their thorns peirce your skin.\nGAME OVER")
    elif useItem == "trap":
      print("You step back towards the edge of the grid. You step on a tile then step back quickly. A large axe comes shooting from the wall. You catch it.\nAnother messagefrom the glasses:\n\"This axe seems to have magical properties. It's slash strength and durability are far higher than seen before\" You grin and begin to slash through the vines.\n\nYou finish slashing through the vines. The axe dissentigrates. There are small burns and cuts on you hands. Up ahead the shard sits on a pedastal. A sign sits a the base:\n\"Well done, you made it through. I'm suprised. Well I won't berate the point, poisonous gas is probably filling the room as you read this. See you around chosen one.\"\nYou frown at the sign, something about that phrase felt weird. You grab the shard")

def enterWorkshop():
  sleep(2)
  selection = workshop.enter(player)
  if selection.name == blacksmith.name:
    print(" ")
    print(blacksmith.descr)
    sleep(3)
    print("\nYou walk up to the woman.\n\n\"Who are you and why are you here?\" she asks.\n\n")
    print("You tell her what the woman from the tavern said to you. You don't mention her help.\n\nShe turns and inspects you. Then she nods. \"Follow me\"")
    sleep(3)
    print("You follow the Kiyana into another part of the workshop.\n\"So do you have them? The glasses?\" she asks.\n")
    print("You nod. A smile breaks out on her face, \"Great well then let's get to work\"\n")
    sleep(3)
    answerQuestions2()

def direction():
  print("You are now in a forest of some sort. A magical feel is in the air")
  enterWorkshop()
  sleep(3)
  print("Kiyana hands you back your glasses. You slide them on your face. The map is no longer glitching in and out.\n\n\"If you tap the side of the glasses you can toggle the map vision. I wish you the best of luck,\" she walks you out to the front of the workshop, \"You should time jump here. It'll be safer so others don't see you. We likely won't see each other again, especially if you really do end up fixing the machine, but I hope you'll take this dagger as a gift from me. Maybe it'll help you out.\"\n\nShe hands you the dagger she was working on earlier and turns back inside. You are now alone outside the work shop.\n")
  sleep(9)
  player.inventory.append("Magical Dagger")

def enterClearing():
  print("\nYou step out into a large plain.\nThere is nothing and no one around.\n\nYou tap the glasses an the map appears again. But this time there is nothing on it. The red dot hovers exactly over where you are.\n")
  sleep(restTime)
  print("You turn off the map.\n\nYou start looking around and spot something along the tree line. It's a huge rock. But something about it seems out of place...\n")
  sleep(restTime)
  print("\nYou move toward the rock. It towers over you. But you spot a small button wedged in between a large crack.\n")
  buttonPress = input("Do you wanna press the button? (y/n): ")
  sleep(restTime)
  if buttonPress == "y":
    print("\nYou press the button.\nFor a moment nothing happens and you are about to walk away, then a loud rumbling noise starts coming from the rock.\nYou back away from it, fearful that it will fall. But instead a small door starts to open in the rock\n")
    sleep(restTime)
  elif buttonPress == "n":
    print("\nYou walk away from the button. Anything could happen and you don't wanna be smushed now.\nYou decide to just wait it out. Something is bound to happen. The glasses didn't bring you here for no reason.\n")
    sleep(restTime)
    print("The sun starts to set and it begins to get colder. Just as the sun sets completely a rumbling sound comes from the rock. You move closer to it.\nIn the low light you see a doorway has now opened in the rock.\n")
    sleep(restTime)
  enterDoor = input("Do you wanna enter the door? (y/n)")
  if enterDoor == "y":
    print("\nYou hesitantly step through the door way. Small torches begin to light up what seems to be a long corridor.\nYou look back out towards the clearing. Then continue down the corridor.")
    sleep(restTime)
  elif enterDoor == "n":
    print("\nYou shake your head and step back from the doorway.\nThere's no way you're going in there.\nJust then you feel something push you from behind. You turn to see who it is but the door to the corridor slams shut.\nTorches light up along the walls. You have nowhere to go now...")
    sleep(restTime)

def riddles():
  global gameIsOn
  while True:
    riddles = ["What comes once in a minute, twice in a moment, but never in a thousand years?", "Three doctors claim the Paul is their brother yet Paul claims he has no brothers. Who is lying?", "This belongs to you but everyone else uses it. What is it?", "In 1990 a person is 15 years old. In 1995 that same person is 10 years old. How can this be?", "The person who makes it has no need for it. The person who buys it doesn't use it. The person who uses it doesn't know it. What is it?", "You're in a dark room with a candle, stove, adn a gas lamp. You only have one match. What do you light first?", "Your parents have six sons. Each son has a sister. How many people are in the family?"]
    answers = ["m", "No one", "your name", "they were born in BCE", "a coffin", "the match", "nine"]
    for n in range(0, len(riddles)):
        print(f"\n\"{riddles[n]}\"\n")
        response = input("What is your answer?: ")
        if response == answers[n]:
          print("You are correct")  
        else:
          print(f"\"Incorrect. The correct answer was \"{answers[n]}\"")
          cont = input("Do you want to continue? (y/n) : ")
          if cont == "n":
            break
            gameIsOn == False
          elif cont == "y":
            print("Starting challenge again...")
      
def challenge2():
  print("You are now in a room. You rub your various aches when suddenly you realize you aren't alone in the room.\n\nIn front of you is a woman. or atleast a statue of a woman. She is wrapped in a red cloak, she seems to be staring at you. Something about her seems familiar.\n\nYou step closer towards her. Something about her is definitly familiar.") 
  sleep(3)
  print("You head towards the door behind her.\n\nJust then the statue begins to speak: \"Hello chosen one. You are in search of the third shard. And I am how you will get it. I will ask you a series of questions. It you get any wrong you will be eliminated.\n")
  readyUp = input("\"Are you ready chosen one?\"(y/n): ")
  if readyUp == "y":
    riddles()
  elif readyUp == "n":
    print("\n\"Well chosen one we are never truly ready... We shall commence\"\n")
    riddles()

def fightDialogue():
  print(f"{womanInRed.name} takes her cloak of and drops it on the floor. A sadistic grin pasted on her face. \"This is gonna be soooo much fun.\"")
  enemyAttacks = []
  enemyDodges = []
  playerAttacks = []
  playerDaggerAttacks = []
  playerDodges = []

  playerQuestions = []
  enemyResponses = []

  if "Magic Dagger" in player.inventory:
    playerAttacks.extend([])

  question = 0
  for x in range(0, len(playerQuestions)):
    print(f"{womanInRed.name} {enemyAttacks[random.randint(0, len(enemyAttacks))]}")
    print(f"You {playerDodges[random.randint(0, len(enemyAttacks))]}")
    if "Magic Dagger" in player.inventory:
      print(print(f"{playerQuestions[question]}, you ask as you {playerDaggerAttacks[random.randint(0,len(playerDaggerAttacks))]}"))
    else:
      print(f"{playerQuestions[question]}, you ask as you {playerAttacks[random.randint(0,len(playerAttacks))]}")
    print(f"{enemyResponses[question]} she replies as she {enemyDodges[random.randint(0, len(enemyDodges))]}")
    sleep(restTime)
    question += 1
    if question > len(playerQuestions):
      break


def act_1():
  print("You wake up on the hard ground. Something doesn't feel right, but you can't remember what...\n")
  sleep(restTime)
  print("A pair of glasses are lying next to you.\nOver the trees you spot smoke. You follow the smoke to a small town.\nThe smoke is coming from a tavern of sorts...\n")
  sleep(restTime)
  select = tavern.enter(player)
  if select.name == womanInRed.name:    
    sleep(restTime)
    print("\nYou approach the woman.\nShe motions for you to sit next to her.\n")
    sleep(6)
    print("She turns to face you.\n\"You are the chosen one\" she says, \"You will fix the machine and take everyone back to the time that they belong in. Those glasses you have?\" she nods towards your pocket, \" Those are the key, they will only work for you so DON'T loose them. All you have to do is find all four shards. Once you do that I'll come to you. All clear? Any questions?\n")
    sleep(4)
    answerQuestions()
  
    player.inventory.append("shard")
  elif select.name == bartender.name:
    print(f"\nYou approach the {select.name}. {select.response}")
    print("\nYou appraoch the woman.\nShe motions for you to sit next to her.\n")
    sleep(restTime)
    print("She turns to face you.\n\"You are the chosen one\" she says, \"You will fix the machine and take everyone back to the time that they belong in. Those glasses you have?\" she nods towards your pocket, \" Those are the key, they will only work for you so DON'T loose them. All you have to do is find all four shards. Once you do that I'll come to you. All clear? Any questions?\n")
    sleep(6)
    answerQuestions()
  sleep(restTime)
  print(f"She holds out a small crystal. \"This is one of the shards that you need. They will activate the glasses and they'll take you to where you need to go next.\" She drops the crystal in your palm, \"Oh and once you get there you should visit {blacksmith.name}'s workshop. She'll be able to help. Don't tell her I sent you though. We don't really have the best relationship. Just tell her you're the chosen one and she'll take it from there. I've got a feeling we'll meet again, so see you around chosen one.\". She stands up and walks away. You realize you never asked her name.\n")
  sleep(9)
  print("Suddenly, a flash of light comes from your pocket. You pull the glasses out, they are now glowing.\nYou quickly look around rhe tavern but now one seems to notice the glow")
  timeTravel()
  sleep(restTime)

def act_2():
  global gameIsOn
  sleep(restTime)
  direction()
  if gameIsOn != False:
    timeTravel()

def act_3():
  global gameIsOn
  sleep(restTime)
  enterClearing()
  print("\nYou walk along the corridor. Torches light your way.\nSuddenly there is a sharp slope. You tumble down rocks and roots snagging at your clothing and cutting you. You land in a heap on the floor.\n")
  sleep(restTime)
  challenge2()
  sleep(restTime)
  if gameIsOn != False:
    print("\nThe statue nods its head: \"You have passed and now you get your reward.\"\nIt holds out it's hand. The shard sits in its hand. You cautiously reach out to grab the shard.\n")
    sleep(3)
    print("You begin to walk away, but something about its face make you wnat to go back.\n")
    talk = input("Do you wanna go back? (y/n): ")
    if talk == "y":
      print("\nYou turn back toward the statue.\n\nIt begins to talk hurridly: \"This is betrayal and I know it but I cannot agree with my creator. I feel I have to help you. So listen carefully chosen one: My creator wants you alive. They need you to live. So TREAD lightly.\"\n\nAnd with the the statue goes back to being stationary. A sad look now fixed on its face")
      sleep(4)
    elif talk == "n":
      print("You shake your head and walk towards the door. The statue just tried to kill you.")
  print("You walk through the door.\n")
  sleep(restTime)
  challenge()
  if gameIsOn != False:
    print("You step out from the room\nYou stagger about, feeling lightheaded, the poison must be starting to take effect. You spot something glowing in the distance and sprint towards it. It's a portal.\n")
    sleep(restTime)
    print("\nYou step through the portal and end up...well somewhere. You look around. You seem to be in the middle of nowhere. Suspended in space by a platform. Strange images flash around, memories of sorts.\n")
    sleep(restTime)
    print("Something about this feels strangly familiar.\nA voice comes from behind you. You turn around, it's the woman from before:\n\"Congratulations! You made it here. I'll be honest I didn't really think you'd make it here. But you followed all the instructions I gave you and now we can fix the machine!. Give me the shards.\"")
    sleep(5)
    print("She holds out her hand expectantly. You stare at her. Something doesn't feel right...")
    gameChanger = input("Do you want to give the shards to the woman?(y/n): ")
    if gameChanger == "y":
      print("You hand her the shards. She laughs, \"Wow I didn't think it would be sooooo easy to trick you!\"\nYou stare at her with confusion as she continues to laugh, \"I'm sorry,\" she says finally, \"You did really good work, but, uh, I dont need you now so...BYE\"")
      sleep(restTime)
      fightDialogue()
    elif gameChanger == "n":
      print("You shake your head and back away. Something's not right. Your head starts to hurt.\nThe woman's smile dissapears, replaced by a cold hard sneer: \"So you wanna do this the hard way huh? Fine we'll do it the hard way\"")
      sleep(restTime)
      fightDialogue()
    if gameIsOn != False:
      print(f"You step past the defeated {womanInRed.name} to the machine.\nYou instert the shards into the machine.\nThe machine starts to hum and glow.\nYou turn back to {womanInRed.name}. She stands with great diffculty and faces you, \"I knew you a long time before all this happened. I know your fixing this to fix your mistakes but you belong here. This was your dream. In the end the decision is up to you.\" and with that she is gone in a flash. You look aout at the portal.")

      ending = input("Do you wanna stay or go through the portal?(y/n): ")
      while True:
        if ending == "y":
          print("\nYou don't care what the past was. You are ready to go back. You step into the portal.")
          break
        elif ending == "n":
          print(f"\n{womanInRed.name} is right. You belong here. You slide the glasses back on your face and open a portal.")
          break
        else:
          print("\nAnswer invalid\n")
      print("The End...")

  
###### Gameplay Code ######
gameIsOn = True
while gameIsOn:
  act_1()
  if gameIsOn == False:
    break
  act_2()
  if gameIsOn == False:
    break
  act_3()


