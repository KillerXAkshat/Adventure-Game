import time
import random


def print_pause(s):
    print(s)
    time.sleep(0.20)


def valid_input(prompt, op1, op2):
    while True:
        choice = input(prompt)
        if choice == op1:
            break
        elif choice == op2:
            break
        else:
            print_pause("I didn't understand")
    return choice


def intro(enemy, weapon):
    print_pause("You find yourself in a Dark room, you can't seem to remember "
                "where are you and why are you there.")
    print_pause("there were two door black and white coloured"
                " you stand up and look around")
    print_pause("You dont have anything to open the door\n")
    search(enemy, weapon)


def search(enemy, weapon):
    print_pause("Press 1 to search for the key in room.")
    print_pause("Press 2 to go straight away to the door")
    print_pause("What would you like to do?")
    choice = valid_input("(Please enter 1 or 2).\n", "1", "2")
    if choice == "1":
        room(enemy, weapon)
    elif choice == "2":
        lock(enemy, weapon)


def room(enemy, weapon):
    print_pause("you looked around and find an unusual shaped key")
    print_pause("you notice that the colour of key is also that of the door"
                " that of the door!")
    print_pause("You pick up the key and put it into your pocket.")
    print_pause("Which door you want to open (1) Black or (2) white?")
    choice = valid_input("(Please enter 1 or 2).\n", "1", "2")
    if choice == "1":
        print_pause("You put the key into the lock turned the lock and"
                    " the gate slowly opens")
        print_pause("you heared sounds of " + enemy + " and a loud buzz"
                    " in your ear.")
        print_pause("There were three " + enemy + " and you have nothing in "
                    " your inventory. So, u can't fight and you are dead. ")
        print_pause("You are defeated")
        end_game()
    elif choice == "2":
        print_pause("You put the key into the lock turned the lock"
                    " and the gate slowly opens")
        print_pause("You find a golden sword there which"
                    " will help you to fight aginst " + enemy + " . ")
        weapon.append("Golden Sword")
    victory(enemy, weapon)


def lock(enemy, weapon):
    print_pause("The door is locked, you can't open it.")
    search(enemy, weapon)


def victory(enemy, weapon):
    print_pause("What do you want to do now (1) unlock Black Door"
                "or (2) Run away?")
    choice = valid_input("(Please enter 1 or 2).\n", "1", "2")
    if choice == "1":
            print_pause("You put the key into the lock turned the lock"
                        " and the gate slowly opens")
            print_pause("you heared sounds of " + enemy + " and a loud buzz"
                        " in your ear.")
            print_pause("But you have golden sword, you grab the sword"
                        " and fight the " + enemy + " and you finally"
                        " defeated them.")
            print_pause("Congratulations! You are Victorious")
            end_game()
    elif choice == "2":
        print_pause("You are loser")
        print_pause("You are Defeated")
        end_game()


def end_game():
    print_pause("Do you like to play again?")
    choice = valid_input("(Please enter 1 or 2).\n", "1", "2")
    if "1" in choice:
        print_pause("Great! lets play again.")
        adventure_game()
    elif "2" in choice:
        print_pause("Thanks for playing!")


def adventure_game():
    enemy_list = ["pirate", "dragon", "murderer", "witch"]
    weapon = []
    enemy = random.choice(enemy_list)
    intro(enemy, weapon)


adventure_game()
