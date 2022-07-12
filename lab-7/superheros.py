#####################################################################                                                                 
 #  Team Edge objects: SUPERHERO CHALLENGES 
 # 
 #   In self challenge you are going to modify self code to do the
 #   the following below. Before you begin, walkthrough the code 
 #   with your coaches.
 #   
 #   1. Change both superhero and nemesis using same class. (Changes: Added hit points, which you get whenever you attack. Prints out total hit poitns at end of game.)
 #   2. Change the variables to modify gameplay and see how it affects (Changes: I changed the lives range and the game started ending shroter, I also changed the delay and the time between rounds got a lot longer)
 #      the game outcomes.
 #   3. Make any improvements you think would make self game better. (Improvements: Moved the sleep function to the fight loops so that you wouldn't have empty rounds, added in some more word to the string literals to help with word flow, changed the lives range because it was really highg before and caused the game to go on for a long time)
 #   4. Complete all the comments to demonstrate you understand the code
 #      Be specific about what each code block is doing.
 #     
 # 
 # ###############################################################/
import random
from time import sleep

print("-------------------  SUPERHERO !!  -------------------")

DELAY = 3
DAMAGE_LIMIT = 5
MAJOR_BLOW = DAMAGE_LIMIT -2
LIVES_TOP_RANGE = 30
LIVES_BOTTOM_RANGE = 10
rounds = 1
game_is_on = True

#COMMENT 1: Defineing the class Superhero
class Superhero:
  def __init__(self, name=None, is_alive=None, friends=None, hit_points=None, is_good=None, attack_power=None):
      self.name = name
      self.is_alive = is_alive
      self.taunts=[]
      self.cries=[]
      self.lives = []
      self.hit_points = 0
    
  def attack(self, enemy):
    global game_is_on
    #COMMENT 2: Sets rules for when a character attack is the game. IF the character and it's enemy is alive then the character will attack.
    if self.is_alive and enemy.is_alive: 
        print("  \n   ")
        damage = random.randint(0,DAMAGE_LIMIT)         
        enemy.lives = enemy.lives[:len(enemy.lives) - damage]
        self.calc_points(damage)
        
        if damage >= MAJOR_BLOW:
          print("Major Blow!")
          #COMMENT 3: IF the damage delt by the attack is greater than or equal to the value set for MAJOR_BLOW, then deal the damage and take the lives away.  
          print(f"{self.name} \: {self.taunts[random.randint(0,len(self.taunts) -1)]} \n")
          print(f"{self.name} deals 💥x {damage} damage to {enemy.name} {enemy.lives} : {len(enemy.lives)}\n")
        
        if len(enemy.lives) <= 0:
          #COMMENT 4: If the lives of the enemy is less than or equal to 0 then stop the game and print to the screen that the enemy is dead and the game is over. If the lives of the character reaches less than or equal to 0 then you would do the same thing.
          enemy.is_alive=False
          game_is_on=False
          print(f"💀💀💀💀💀💀 {enemy.name} has been slain!!! 💀💀💀💀💀 ")
          print(f"{self.name}'s hit points are: {self.hit_points}. {enemy.name}'s hit points were: {enemy.hit_points}")
          print("GAME OVER")
          
        if len(self.lives) <= 0:
          self.is_alive = False
          game_is_on = False
          print(f"💀💀💀💀💀💀 {self.name} has been slain!!! 💀💀💀💀💀")
          print(f"{enemy.name}'s hit points are: {enemy.hit_points}. {self.name}'s hit points were: {self.hit_points}")
          print(" GAME OVER ")
      
  def fill_health(self):
      #COMMENT 5: For a random number in the range of bottom life range and top life range add that number to the lives that the character has.
      amt = random.randint(LIVES_BOTTOM_RANGE, LIVES_TOP_RANGE)
        
      for i in range(0, amt):
          self.lives.append("💙")
  def calc_points(self, damage):
    # Add more points for high damage and less points for less damage
    hit_points = 0
    if damage >= MAJOR_BLOW:
      hit_points += 5
    elif damage < MAJOR_BLOW:
      hit_points += 2
    
    # update points for self and enemy
    self.hit_points += hit_points


#COMMENT 6: Creating a new character using the class Superhero. Fill in the previously empty values from Superhero and add in the fill_health function.
batman = Superhero()
batman.name = "Batman 🦸‍♂️"
batman.is_alive = True 
batman.lives = []
batman.taunts = ["The Dark Knight always wins!" , "You can't hang with the bat man" , "Meet my fist, scumbag" , "You Suck!"]
batman.cries=["Ouch!" , "UFF!" , "Gaaaaaaa" , "No!!!!!"]
batman.fill_health()
 
joker = Superhero()
joker.name = "Joker 🦹‍♂️"
joker.is_alive = True
joker.lives=[]
joker.taunts =["You are a schmemer" , "Don't mess with the Joker!" , "Pick your face off the ground, you might need it!", "Getting tired of the beatings?"]
joker.cries = ["Aaaa!" , "Goh!" , "Hmph!" ,"You will pay for self"]
joker.fill_health()


print(f"{joker.name} :  {joker.lives} - {len(joker.lives)}")
print(f"{batman.name} : {batman.lives} -  {len(batman.lives)}")
print(f"{batman.name} 💬 {batman.taunts[1]}  \n")
print(f"{joker.name} 💬 {joker.taunts[1]}  \n")


#COMMENT 7: Sets up the rounds system. Passes in parameters a and b. Tells the user what round they are on. Has a attack b and b attack a. Then it reassigns the value for rounds then it sleeps for the value DELAY. Then it runs again.
def fight(a, b):
    global rounds

    print(" ------------- ROUND -------------> " + str(rounds))
    a.attack(b)
    b.attack(a)
    rounds += 1
    sleep(DELAY)
  
#COMMENT 8: While the game is one batman will attacjk joker and joker batman using the fight function that has been defined above. Then it just prints a new line
while game_is_on:
    fight(batman,joker) 
    print(" \n") 