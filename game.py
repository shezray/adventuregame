import time


def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(2)


def intro():
    print_pause("You find yourself stranded on an island filled with zombies ")
    print_pause("You don't see anyone around you, you are alone.")
    print_pause("In front of you is a small abandoned hut.")
    print_pause("To your right is a small boat chained to "
                "a tree at the seashore.")



def small_hut(items):
    print_pause("You approach the entrance to the small hut")
    print_pause("It is eerily quiet at first")
    print_pause("After a few moments, a zombie approaches "
                "from behind you!")
    
    if "key" in items:
        print_pause("You have defeated the zombie "
                    "and have found the magic key!")
        print_pause("There is nothing more to do here now.")
    else:
        print_pause("You attack the zombie and find a magic key "
                    "in his pocket!")
        items.append("key")
    print_pause("You head back outside.")
    outside(items)


def boat(items):
    print_pause("You approach the boat at the shore.")
    print_pause("You notice that it needs a key to  "
                "unlock the chain.")
    if "unlock" in items:
        print_pause("You cannot use the boat without a key ")
        print_pause("There isn't much to do here.")
    else:
        print_pause("You've got the key to unlock the boat!")
        if "key" in items:
            print_pause("You insert the key into the lock"
                        "and are able to access the boat to escape!")

    print_pause("You head back out to where you started")
    outside(items)
    play_again()



def outside(items):
    print_pause("Enter 1 to go inside the small hut "
                "Enter 2 to go to the boat")
    place = input("1. small hut\n"
                  "2. boat\n")
    if place == '1':
        small_hut(items)
    elif place == '2':
        boat(items)

def play_again():
    response = valid_input("Would you like to play again? "
                              "Please say 'yes' or 'no'.\n",
                              "yes", "no")
    if "no" in response:
        print_pause("OK, goodbye!")
    elif "yes" in response:
        print_pause("Very good, I'm happy to take another order.")
        play_again()

def play_game():
    items = []
    intro()
    outside(items)


play_game()