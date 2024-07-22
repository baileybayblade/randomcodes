import time
import random

global player_weapon
player_weapon = 'Dagger'
global weapons
weapons = ['Sword', 'Wand', 'Claymore', 'Spear']
global new_player_weapon
new_player_weapon = random.choice(weapons)
global player_input
player_input = ""

def main():
    print("You find yourself standing in an open field, filled with grass and yellow wildflowers.")
    time.sleep(2)
    print("Rumor has it that an evil dragon is somewhere around here, and has been terrifying the nearby village.")
    time.sleep(2)
    print("In front of you is a forest.")
    time.sleep(2)
    print("To your right is a dark cave.")
    time.sleep(2)
    print("In your hand you hold your trusty (but not very effective) dagger.")
    time.sleep(2)
    print('What would you like to do?') 
    player_choice()

"""
def player_choice():
    global player_input
    player_input = ""
    while player_input not in ['1','2']:
       player_input = input("(Please Enter 1 or 2): ")
    if player_input == '1':
       forest()
    elif player_input == '2':
       cave(player_weapon)
"""

def play_again():
    global player_input
    player_input = ""
    time.sleep(2)
    print('Would you like to play again? [Y/N]: ')
    while not player_input in ['Y','N']:
        player_input = input('(Please enter Y/N): ')
    if player_input == 'Y':
        main()
    elif player_input == 'N':
        print('Goodbye! :3')
    return

#after the player picks 2, where they should now pick 1 to finish the game properly.
def main_after_cave():
    #brings the user to the village AFTER the cave - this can only happen after picking 2.
    global player_input
    player_input = ""
    time.sleep(2)
    print('You have returned to the main village.')
    time.sleep(2)
    print(f'You now have a {new_player_weapon}.')
    time.sleep(2)
    print('Now you can safely head into the forest.')
    time.sleep(2)
    print('Please enter 1 to proceed: ')
    while not player_input == '1':
        player_input = input('Please enter 1: ')
    if player_input == '1':
        forest()
    if player_input == '2':
        print('You already visited the cave.')
        time.sleep(2)
        print('Please enter 1 to proceed into the forest.')
        pass

#if the player picks 2 first (aka what SHOULD happen)
def cave(player_weapon):
    global points
    points = 0
    x = ", ".join(weapons)
    while player_input == '2':
        print(f"You enter the cave and find a:", x)
        time.sleep(2)
        print(f"Would you like to change your weapon? Your current weapon is {player_weapon}.")
        time.sleep(2)
        weapon_request = ""
        while weapon_request not in ["Y","N"]:
            weapon_request = input("Please Enter Y/N: ")
        if weapon_request == "Y":
            player_weapon == new_player_weapon
            print(f'Your weapon is now {new_player_weapon}')
            time.sleep(2)
            print('You head back to the main village.')
            time.sleep(2)
            points += 1
            print(f'Your points have increased! You now have {points} points!')
            main_after_cave()
            break
        if weapon_request == "N":
            print('You take the new weapon, anyway.')
            print(f'Your weapon is now {new_player_weapon}')
            time.sleep(2)
            player_weapon == new_player_weapon
            points += 1
            print(f'Your points have increased! You now have {points} points!')
            main_after_cave()
            break

"""
def forest():
    global points
    points = 0
    while player_input == '1':
        if player_weapon == new_player_weapon:
            time.sleep(2)
            print("You head towards the forest and find the evil dragon.")
            time.sleep(2)
            print(f"Before it can strike you, you kill it with your {new_player_weapon}. You win!")
            time.sleep(2)
            if points >= 0:
                print(f"You now have {points} points! Nice one. ;3")
            if points == 0:
                print(f'But... you have {points} points! 3:')
            return
        elif player_weapon != new_player_weapon:
            print('You accidentally find the evil dragon!')
            time.sleep(2)
            print('But due to your bad weapon, the dragon strikes first! You lose!')
            time.sleep(2)
            points -= 1
            print('And your points have decreased...')
            return
"""

#if the player picks 1 first
def forest():
    global points
    while player_input == '1':
        if points <= 1:
            time.sleep(2)
            print("You head towards the forest and find the evil dragon.")
            time.sleep(2)
            print(f"Before it can strike you, you kill it with your {new_player_weapon}. You win!")
            time.sleep(2)
            return
        if points <= 0:
            print('You accidentally find the evil dragon!')
            time.sleep(2)
            print('But due to your bad weapon, the dragon strikes first! You lose!')
            time.sleep(2)

            return

def player_choice():
    global player_input
    player_input = ""
    while player_input not in ['1','2']:
       player_input = input("(Please Enter 1 or 2): ")
    if player_input == '1':
       forest()
    elif player_input == '2':
       cave(player_weapon)

main()
