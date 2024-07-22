#!/bin/python3
#COSC1519 Introduction to Programming
#A2 Programming Project
#Student name: Elissa Van
#Student number: s3935201
def title():
  print('=======================================================')
  print("...Welcome to CHOICES, a text-based game...")
  print('=======================================================')
title()

def scene_1():
  print("It is 4:30pm...you are at work...")
  print("Making drinks at Shockalatté...")
  print("A new customer arrives and orders their drink.")
  print("\n>'Hello, my name is Evi. What can I get for you today?'")
  print(">'Hi there! Hmm...What do you suggest?'\n")
scene_1()

order = None
while order != 3: 
  print("What do you say?")
  order = input("""1 - There is some sweets left. Would you like a slice of cake?
2 - We are known for our drinks. How about a coffee?
3 - How about a coffee paired with something sweet for a balance? [best choice]\n""")
  if order == '1':
    print(">'Hmm...Is there anything else?'")
    print("--------------------------------")
  elif order == '2':
    print(">'Hmm...Anything else?'")
    print("--------------------------------")
  elif order == '3':
    print(">'In that case, I will have a slice of cake and coffee to go please, thank you.'")
    print("--------------------------------")
    break
  else:
    print("Only numerical values (1, 2, 3) accepted. Please try again!")

print("""The clock shows 5:05pm as you serve the final customer for today...
Home sweet home...
Here you come...\n""")

to_continue = input("<Please press Enter to continue>\n")

def scene_2():
  street_name = input("Walking home from work, your house is located on what street?")
  print("You make a turn on", street_name, "and arrive at your house, there you see a package has been delivered to your front door.")
  l_name = input("What is the last name on the shipping label?")
  print("'Evi...", l_name + "'", "confirming that this package belongs to you, you finally head inside.")
  print("""Inside, Your Meowjesty The 3rd greets you, meowing loudly for you to feed him...
After Your Meowjesty The 3rd is well fed and taken care of...
You open your delivery package...""")
  print("What 'weapon' is inside the delivery package?")
scene_2()

weapon_choice = '1 - Spellbook', '2 - Wand', '3 - Crystal Ball', '4 - Staff', '? - Any other entry will default to the chosen weapon: Talisman'
for weap in weapon_choice:
  print(weap)
chosen_w = 'Spellbook Wand Crystal Ball Staff Talisman'
chosen_weapon = None
while chosen_weapon == None:
  try:
    chosen_weapon = int(input("Choose a number between 1-4:"))
    if chosen_weapon == 1:
     print("You have chosen the weapon:", chosen_w[0:9] + ". Excellent choice, now then let the adventure of Evi and her", chosen_w[0:9], "begin!\n")
    elif chosen_weapon == 2:
      print("You have chosen the weapon:", chosen_w[10:14] + ". Excellent choice, now then let the adventure of Evi and her", chosen_w[10:14], "begin!\n")
    elif chosen_weapon == 3:
      print("You have chosen the weapon:", chosen_w[15:27] + ". Excellent choice, now then let the adventure of Evi and her", chosen_w[15:27], "begin!\n")
    elif chosen_weapon == 4:
      print("You have chosen the weapon:", chosen_w[28:33] + ". Excellent choice, now then let the adventure of Evi and her", chosen_w[28:33], "begin!\n")
    else:
      print("You did not enter an integer between 1-4, defaulting to:", chosen_w[34:42] + ". Not bad, well then, let the adventure of Evi and her", chosen_w[34:42], "begin!\n")
  except:
    print("Please enter integers only.")
    continue

to_continue = input("<Please press Enter to continue>\n")

def scene_3():
  print("brzzt brzzt... brzzt brzzt... brzzt brzzt...")
  print("Your SAMiSung is vibrating like crazy with every incoming message before it starts to ring...")
  print("You pick up...\n")
  print(">'Heyo Evi! It's me, Luci! Did you check my messages yet? There's a new event starting and everyone's ready to raid! What do you say?!'\n")
scene_3()

print("1 - Sure, I'm down to murder some enemies! [continue game]")
print("2 - Umm...I'm not sure...kinda tired.")
print("3 - Nah, you guys play without me, I'm kinda sleepy right now.")
while True:
  option = None
  option = input("You joining us?!") 
  if option == '1':
    print("\nYay! We're starting at 10pm, so make sure you're logged in before then and meet us all at the front entrance of the Witch's Dungeon.\n")
    print("You head over to your device and log on just before 10pm...\n")
    to_continue = input("<Please press Enter to continue>\n")
    break
  else:
    if option == '2':
      print("\nCome on! It's the weekend tomorrow anyways, you can sleep then!")
      print("---------------------------------------------------------------")
    else:
      if option == '3':
        print("zzz...Evi has gone to bed...zzz")
        print('===================================')
        print("...Thank you for playing CHOICES...")
        print('===================================')
        exit()
      else:
        print("Please enter a numerical value from 1-3.")
        print("----------------------------------------")

def scene_4():
  print("~|Evi is online|~\n")
  print("After logging on you make your way over to the meetup destination and join up with the team.")
  print("As everyone gets ready to enter the dungeon, you too, prepare yourself for the battle.")
  print("Upon entering you encounter the dungeon's guardian. It appears to be a fire type.\n")
  print("The Fire Dungeon Guardian's health point is 50. What will you do?")
scene_4()

import random
player_name = "Evi"
player_health = 50
enemy_name = "Fire Dungeon Guardian"
enemy_health = 50
def player_attack():
  global enemy_health
  damage_dealth = random.randint(5, 15)
  player_skills = ['shoots a blue fireball', 'casts a spell', 'summons icicle blades']
  skills = '1 - Shoot a blue fireball [ineffective]', '2 - Cast a spell [some damage]', '3 - Summon icicle blades [super effective]'
  for skill in skills:
    print(skill)
  attack = input("What will you do?")
  if attack == '1':
    print(player_name, player_skills[0] + ".")
    print("Luci stares at you... Evi! What are you doing?!")
    print("That's a fire guardian!")
    print("Fire spells aren't going to be effective at all!")
    print(enemy_name, "takes 0 damage.")
    print(enemy_name, "has", enemy_health, "health points left.")
    print("----------------------------------------------------")
  elif attack == '2':
    print(player_name, player_skills[1] + ".")
    enemy_health = enemy_health - damage_dealth
    print(enemy_name, "takes", damage_dealth, "damage.")
    print(enemy_name, "has", enemy_health, "health points left.")
    print("----------------------------------------------------")
  elif attack == '3':
    print(player_name, player_skills[2] + ".")
    print("It was super effective.")
    enemy_health = enemy_health - enemy_health
    print(enemy_name, "takes massive damage.")
    print(enemy_name, "has 0 health points left.")
    print(enemy_name, "has been slain.")
    print("----------------------------------------------------")
    print("Defeating the", enemy_name, "has made you much stronger and taught you new skills...")
    print("Your team proceeds deeper into the dungeon floor...\n")
    to_continue = input("<Please press Enter to continue>\n")
  else:
    print("Please enter integers: '1', '2', '3' only! Otherwise", player_name, "can't understand how to attack.")
    print("----------------------------------------------------")
def enemy_attack():
  global player_health
  damage_dealth = random.randint(4, 8)
  enemy_skills = ['stomp', 'spitfire', 'bodyslam']
  print(enemy_name, "uses", random.choice(enemy_skills) + ".")
  print("It inflicts", damage_dealth, "damage.")
  player_health = player_health - damage_dealth
  print(player_name, "has", player_health, "health points left.")
  print("-----------------------------------------------------")
while enemy_health > 0 and player_health > 0:
  player_attack()
  if enemy_health > 0:
    enemy_attack()
  if player_health < 0:
    print("Uh oh", player_name, "has no more health points left.")
    print(player_name, "has been slain.")
    print("GAME OVER")
    print('===================================')
    print("...Thank you for playing CHOICES...")
    print('===================================')
    exit()
  if enemy_health < 0 and player_health > 0:
    print(enemy_name, "has been slain.")
    print("Defeating the", enemy_name, "has made you much stronger and taught you new skills...")
    print("Your team proceeds deeper into the dungeon floor...\n")
    to_continue = input("<Please press Enter to continue>\n")

def scene_5():
  print("Braving deeper your team comes across a hidden room and discover that it's full of treasure chests...but each treasure chest is possessed by an evil spirit...")
  print("It was a trap!")
  print("Your team is now surrounded...you must defeat them one by one to make it out alive...")
scene_5()
def ability():
  abilities = '1 - Create a wall of hellfire [high damage]', '2 - Manipulate gravity [not very effective]', '3 - Summon a familiar [low damage]', '4 - Perform an exorcism [one shot]'
  for abili in abilities:
    print(abili)
  
import random
import math
player_name = "Evi"
enemy1 = "Red Spirit"
enemy1_health = 40
enemy2 = "Gold Spirit"
enemy2_health = 50
enemy3 = "Blue Spirit"
enemy3_health = 60
enemy4 = "Black Spirit"
enemy4_health = 70

print("\nRed Spirit approaches...")
def first_battle():
  global enemy1_health
  print(enemy1, "has", enemy1_health, "health points.")
  player_abilities = ['creates a wall of hellfire', 'manipulates gravity', 'summons a familiar', 'performs an exorcism']
  ability()
  attack = input("What will you choose to do?")
  print("------------------------------------------------")
  if attack == '1':
    damage_dealth = round(random.random()*10+10,1)
    enemy1_health = enemy1_health - damage_dealth
    print(player_name, player_abilities[0] + ".")
    print(enemy1,"takes", damage_dealth, "damage.")
    print(enemy1, "has", enemy1_health, "health points left.")
    print("------------------------------------------------")
  elif attack == '2':
    damage_dealth = round(random.random()*5,1)
    enemy1_health = enemy1_health - damage_dealth
    print(player_name, player_abilities[1] + ".")
    enemy1_health = enemy1_health - damage_dealth
    print(enemy1, "takes", damage_dealth, "damage.")
    print(enemy1, "has", enemy1_health, "health points left.")
    print("------------------------------------------------")
  elif attack == '3':
    damage_dealth = round(random.random()*5+5,1)
    enemy1_health = enemy1_health - damage_dealth
    print(player_name, player_abilities[2] + ".")
    enemy1_health = enemy1_health - damage_dealth
    print(enemy1, "takes", damage_dealth, "damage.")
    print(enemy1, "has", enemy1_health, "health points left.")
    print("------------------------------------------------")
  elif attack == '4':
    print(player_name, player_abilities[3] + ".")
    print("It was super effective.")
    enemy1_health = enemy1_health - enemy1_health
    print(enemy1, "has been exorcised and freed from its curse.")
    print(enemy1, "has floated away.")
    print("Good job!")
    print("------------------------------------------------")
  else:
    print("Evi doesn't understand you. Please enter only numbers between 1-4.")
    print("------------------------------------------------------------------")
while enemy1_health > 0:
  first_battle()
  if enemy1_health < 0:
    print(enemy1, "has been defeated.")
    print("Good job!")
    print("------------------------------------------------\n")

print("Gold Spirit approaches...")
def second_battle():
  global enemy2_health
  print(enemy2, "has", enemy2_health, "health points.")
  player_abilities = ['creates a wall of hellfire', 'manipulates gravity', 'summons a familiar', 'performs an exorcism']
  ability()
  attack = input("What will you choose to do?")
  print("------------------------------------------------")
  if attack == '1':
    damage_dealth = round(random.random()*10+10,1)
    enemy2_health = enemy2_health - damage_dealth
    print(player_name, player_abilities[0] + ".")
    print(enemy2,"takes", damage_dealth, "damage.")
    print(enemy2, "has", enemy2_health, "health points left.")
    print("------------------------------------------------")
  elif attack == '2':
    damage_dealth = round(random.random()*5,1)
    enemy2_health = enemy2_health - damage_dealth
    print(player_name, player_abilities[1] + ".")
    enemy2_health = enemy2_health - damage_dealth
    print(enemy2, "takes", damage_dealth, "damage.")
    print(enemy2, "has", enemy2_health, "health points left.")
    print("------------------------------------------------")
  elif attack == '3':
    damage_dealth = round(random.random()*5+5,1)
    enemy2_health = enemy2_health - damage_dealth
    print(player_name, player_abilities[2] + ".")
    enemy2_health = enemy2_health - damage_dealth
    print(enemy2, "takes", damage_dealth, "damage.")
    print(enemy2, "has", enemy2_health, "health points left.")
    print("------------------------------------------------")
  elif attack == '4':
    print(player_name, player_abilities[3] + ".")
    print("It was super effective.")
    enemy2_health = enemy2_health - enemy2_health
    print(enemy2, "has been exorcised and freed from its curse.")
    print(enemy2, "has floated away.")
    print("Nice! Keep going!")
    print("------------------------------------------------")
  else:
    print("Evi doesn't understand you. Please enter only numbers between 1-4.")
    print("------------------------------------------------------------------")
while enemy2_health > 0:
  second_battle()
  if enemy2_health < 0:
    print(enemy2, "has been defeated.")
    print("Nice! Keep going!")
    print("------------------------------------------------\n")

print("Blue Spirit approaches...")
def third_battle():
  global enemy3_health
  print(enemy3, "has", enemy3_health, "health points.")
  player_abilities = ['creates a wall of hellfire', 'manipulates gravity', 'summons a familiar', 'performs an exorcism']
  ability()
  attack = input("What will you choose to do?")
  print("------------------------------------------------")
  if attack == '1':
    damage_dealth = round(random.random()*10+10,1)
    enemy3_health = enemy3_health - damage_dealth
    print(player_name, player_abilities[0] + ".")
    print(enemy3,"takes", damage_dealth, "damage.")
    print(enemy3, "has", enemy3_health, "health points left.")
    print("------------------------------------------------")
  elif attack == '2':
    damage_dealth = round(random.random()*5,1)
    enemy3_health = enemy3_health - damage_dealth
    print(player_name, player_abilities[1] + ".")
    enemy3_health = enemy3_health - damage_dealth
    print(enemy3, "takes", damage_dealth, "damage.")
    print(enemy3, "has", enemy3_health, "health points left.")
    print("------------------------------------------------")
  elif attack == '3':
    damage_dealth = round(random.random()*5+5,1)
    enemy3_health = enemy3_health - damage_dealth
    print(player_name, player_abilities[2] + ".")
    enemy3_health = enemy3_health - damage_dealth
    print(enemy3, "takes", damage_dealth, "damage.")
    print(enemy3, "has", enemy3_health, "health points left.")
    print("------------------------------------------------")
  elif attack == '4':
    print(player_name, player_abilities[3] + ".")
    print("It was super effective.")
    enemy3_health = enemy3_health - enemy3_health
    print(enemy3, "has been exorcised and freed from its curse.")
    print(enemy3, "has floated away.")
    print("Last one! Let's go!")
    print("------------------------------------------------")
  else:
    print("Evi doesn't understand you. Please enter only numbers between 1-4.")
    print("------------------------------------------------------------------")
while enemy3_health > 0:
  third_battle()
  if enemy3_health < 0:
    print(enemy3, "has been defeated.")
    print("Last one! Let's go!")
    print("------------------------------------------------\n")

print("Black Spirit approaches...")
def final_battle():
  global enemy4_health
  print(enemy4, "has", enemy4_health, "health points.")
  player_abilities = ['creates a wall of hellfire', 'manipulates gravity', 'summons a familiar', 'performs an exorcism']
  ability()
  attack = input("What will you choose to do?")
  print("------------------------------------------------")
  if attack == '1':
    damage_dealth = round(random.random()*10+10,1)
    enemy4_health = enemy4_health - damage_dealth
    print(player_name, player_abilities[0] + ".")
    print(enemy4,"takes", damage_dealth, "damage.")
    print(enemy4, "has", enemy4_health, "health points left.")
    print("------------------------------------------------")
  elif attack == '2':
    damage_dealth = round(random.random()*5,1)
    enemy4_health = enemy4_health - damage_dealth
    print(player_name, player_abilities[1] + ".")
    enemy4_health = enemy4_health - damage_dealth
    print(enemy4, "takes", damage_dealth, "damage.")
    print(enemy4, "has", enemy4_health, "health points left.")
    print("------------------------------------------------")
  elif attack == '3':
    damage_dealth = round(random.random()*5+5,1)
    enemy4_health = enemy4_health - damage_dealth
    print(player_name, player_abilities[2] + ".")
    enemy4_health = enemy4_health - damage_dealth
    print(enemy4, "takes", damage_dealth, "damage.")
    print(enemy4, "has", enemy4_health, "health points left.")
    print("------------------------------------------------")
  elif attack == '4':
    print(player_name, player_abilities[3] + ".")
    print("It was super effective.")
    enemy4_health = enemy4_health - enemy4_health
    print(enemy4, "has been exorcised and freed from its curse.")
    print(enemy4, "has floated away.")
    print("------------------------------------------------")
  else:
    print("Evi doesn't understand you. Please enter only numbers between 1-4.")
    print("------------------------------------------------------------------")
while enemy4_health > 0:
  final_battle()
  if enemy4_health < 0:
    print(enemy4, "has been defeated.")
    print("------------------------------------------------\n")

print("""Well done! All monsters have been slain...
You're free to leave the hidden room...\n""")

to_continue = input("<Please press Enter to continue>\n")

def scene_6():
  print("Upon leaving the hidden room, you hear something rumbling in the distance...")
  print("BOOM! BOOM! BOOM!\n")
  to_continue = input("<Please press Enter to continue>\n")
  print("Suddenly the ground beneath you begins to shake...")
  print("As it crumbles away into the swallowing darkness...\n")
  to_continue = input("<Please press Enter to continue>\n")
  print("Time is running out!")
  print("The dungeon floor is collasping in on itself!\n")
  to_continue = input("<Please press Enter to continue>\n")
  print("Quick! Do something!!")
scene_6()

team_count3 = 3
team_count2 = 2
team_count1 = 1
def decision():
  decisions = "1 - Leave now by teleporting outside [Safety first!]","2 - Stay and push on for the loot! [I'm not afraid!]" ,"3 - Ignore the earthquake and push on! Teleport outside only as a last resort!! [Good thinking! ...Or bad idea!?]"
  for dec in decisions:
    print(dec)   
def alternative_3survived():
  while team_count3 >= 0:
    team_count2 = team_count3 - 1
    break
  print("------------------------------------------------------")
  print("Uh oh...", team_count3, "of us entered now there's only", team_count2, "members left...")
  print("------------------------------------------------------")
def alternative_2survived():
  while team_count2 >= 0:
    team_count1 = team_count2 - 1
    break
  print("-------------------------------------------------------")
  print("Oh no... We lost another one! Only", team_count1, "team member left...")
  print("-------------------------------------------------------")
def alternative_1survived():
  while team_count3 >= 0:
    team_count0 = team_count1 - 1
    break
  print("As you travel deeper and deeper into the dungeon, the earth trembles with every step...")
  print("Realising that your team members are no longer beside you...and that the fallen boulders have blocked your exit...")
  print("You, too will soon succumb to the darkness down below...")
  print("---------------------------")
  print("Oh dear... No one's left...")
  print("BAD ENDING - NO SURVIVORS")
  print("---------------------------")
  print('==================================================================')
  print("...Thank you for playing CHOICES...Evi has had a fun time today...")
  print('==================================================================')
def final_decision():
  decision()
  try:
    think_fast = int(input("\nThink fast! What will you choose to do?\n"))
    if think_fast == 1:
      print("That was a close call! Everyone escaped the disaster just in time...")
      print("Unfortunately, in the absolute mayhem, all the loot had been forgotten...\n")
      print("----------------------------------------------------------")
      print("Congratulations, you made it out alive with no lives lost!")
      print("GOOD ENDING - EVERYONE SURVIVED")
      print("----------------------------------------------------------")
      print('==================================================================')
      print("...Thank you for playing CHOICES...Evi has had a fun time today...")
      print('==================================================================')
    elif think_fast == 2 or think_fast == 3:
      alternative_3survived()
      final_decision2()
    else:
      print("---------------------------------------------------------------")
      print("Now is not the time! Quick enter an integer between 1-3! C'mon!")
      print("---------------------------------------------------------------")
      return final_decision()
  except:
    print("---------------------------------------------------------------")
    print("Now is not the time! Quick enter an integer between 1-3! C'mon!")
    print("---------------------------------------------------------------")
    return final_decision()
def final_decision2():
  decision()
  try:
    think_fast = int(input("Think fast! What will you choose to do?\n"))
    if think_fast == 1:
      print("Finally making it outside, you collasped to the ground in shock at the turn of events...")
      print("Turning to look at your only remaining team mate... You finally process what had just happened.")
      print("-----------------------------------------------------------")
      print("Phew... At least a team member and yourself are still alive.")
      print("SAD ENDING - 2 SURVIVORS")
      print("-----------------------------------------------------------")
      print('==================================================================')
      print("...Thank you for playing CHOICES...Evi has had a fun time today...")
      print('==================================================================')
    elif think_fast == 2 or think_fast == 3:
      alternative_2survived()
      final_decision3()
    else:
      print("---------------------------------------------------------------")
      print("Now is not the time! Quick enter an integer between 1-3! C'mon!")
      print("---------------------------------------------------------------")
      return final_decision2()
  except:
    print("---------------------------------------------------------------")
    print("Now is not the time! Quick enter an integer between 1-3! C'mon!")
    print("---------------------------------------------------------------")
    return final_decision2()
def final_decision3():
  decision()
  try:
    think_fast = int(input("Think fast! What will you choose to do?\n"))
    if think_fast == 1:
      print("Everyone is gone...")
      print("Look on the brightside, at least you made it out alive.")
      print("--------------------------")
      print("TRAGIC ENDING - 1 SURVIVOR")
      print("--------------------------")
      print('==================================================================')
      print("...Thank you for playing CHOICES...Evi has had a fun time today...")
      print('==================================================================')
    elif think_fast == 2 or think_fast == 3:
      alternative_1survived()
    else:
      print("---------------------------------------------------------------")
      print("Now is not the time! Quick enter an integer between 1-3! C'mon!")
      print("---------------------------------------------------------------")
      return final_decision3()
  except:
    print("---------------------------------------------------------------")
    print("Now is not the time! Quick enter an integer between 1-3! C'mon!")
    print("---------------------------------------------------------------")
    return final_decision3()

team_count3 = 3
while team_count3 > 0:
  final_decision()
  break