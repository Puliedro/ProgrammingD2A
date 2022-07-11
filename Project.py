
#██████   ██████   ██████ ██   ██        ██████   █████  ██████  ███████ ██████         ███████  ██████ ██ ███████ ███████  ██████  ██████  ███████ 
#██   ██ ██    ██ ██      ██  ██         ██   ██ ██   ██ ██   ██ ██      ██   ██        ██      ██      ██ ██      ██      ██    ██ ██   ██ ██      
#██████  ██    ██ ██      █████          ██████  ███████ ██████  █████   ██████         ███████ ██      ██ ███████ ███████ ██    ██ ██████  ███████ 
#██   ██ ██    ██ ██      ██  ██         ██      ██   ██ ██      ██      ██   ██             ██ ██      ██      ██      ██ ██    ██ ██   ██      ██ 
#██   ██  ██████   ██████ ██   ██ ▄█     ██      ██   ██ ██      ███████ ██   ██ ▄█     ███████  ██████ ██ ███████ ███████  ██████  ██   ██ ███████ 

#                                        ▓█████ ▒██   ██▒▄▄▄█████▓ ██▀███  ▓█████  ███▄ ▄███▓▓█████ 
#                                        ▓█   ▀ ▒▒ █ █ ▒░▓  ██▒ ▓▒▓██ ▒ ██▒▓█   ▀ ▓██▒▀█▀ ██▒▓█   ▀ 
#                                        ▒███   ░░  █   ░▒ ▓██░ ▒░▓██ ░▄█ ▒▒███   ▓██    ▓██░▒███   
#                                        ▒▓█  ▄  ░ █ █ ▒ ░ ▓██▓ ░ ▒██▀▀█▄  ▒▓█  ▄ ▒██    ▒██ ▒▓█  ▄ 
#                                        ░▒████▒▒██▒ ▒██▒  ▒██▒ ░ ░██▓ ▒██▒░▒████▒▒██▒   ░██▒░▒████▒
#                                        ░░ ▒░ ░▒▒ ░ ░▓ ░  ▒ ░░   ░ ▒▓ ░▒▓░░░ ▒░ ░░ ▒░   ░  ░░░ ▒░ ░
#                                        ░ ░  ░░░   ░▒ ░    ░      ░▒ ░ ▒░ ░ ░  ░░  ░      ░ ░ ░  ░
#                                        ░    ░    ░    ░        ░░   ░    ░   ░      ░      ░   
#                                        ░  ░ ░    ░              ░        ░  ░       ░      ░  ░
                                                           

# This App will present a fun version of the Rocks, Papers , Scissors game that we always play.
# The idea is for the machine to choose randomly between rocks, papers, scissors and play with you! It will track the amount of times you've won and lost!


#Importing useful libraries
import random 
import time

#Function to make the selection of the machine randomized
def machineSelection():
    return random.choices(options, weights=(35,35,30), k=1)

#Function to print the game
def game():
    print("You have made your choice!\n")
    time.sleep(1)
    print("1...\n")
    time.sleep(1)
    print("2..\n")
    time.sleep(1)
    print("3...\n")
    time.sleep(1)
    print("Go!\nYou: " + userSelection + "\nBot: " + macSelectionString)
    
       
    
#Getting the values of the machine selection
# 1 = Rock, 2=Paper, 3=Scissors
options = [1,2,3]
macSelection = machineSelection()

#Assigning a string to each value
if macSelection == [1]:
    macSelectionString = "Rock"
elif macSelection == [2]:
    macSelectionString = "Paper"
elif macSelection == [3]:
    macSelectionString = "Scissors"
#print(macSelectionString)

#Initializing game and logic
print("Welcome to Rock, Paper, Scissors EXTREME, a good way of having fun against a super intelligent machine\n ")
i=0
while i == 0:
    userSelection = input("Make your selection! Please enter either Rock, Paper or Scissors!\n")
    if userSelection == "Rock":
        i += 1
        game()
        if (macSelection == [1]):
            print("\nBot: It's a tie! well played!\nThe result was a TIE. Thank you so much for playing")
        elif (macSelection == [2]):
            print("\nBot: Yasss!!! I won!! \nYou lost! Try again!. Thank you so much for playing")
        elif (macSelection == [3]):
            print("\nBot: Noooo! I lost!! aww! I'll win next time!\nYou've won!. Thank you so much for playing")
    elif userSelection == "Paper":
        i += 1
        game()
        if (macSelection == [2]):
            print("\nBot: It's a tie! well played!\nThe result was a TIE. Thank you so much for playing")
        elif (macSelection == [3]):
            print("\nBot: Yasss!!! I won!! \nYou lost! Try again!. Thank you so much for playing")
        elif (macSelection == [1]):
            print("\nBot: Noooo! I lost!! aww! I'll win next time!\nYou've won!. Thank you so much for playing")
    elif userSelection == "Scissors":
        i += 1
        game()
        if (macSelection == [3]):
            print("\nBot: It's a tie! well played!\nThe result was a TIE. Thank you so much for playing")
        elif (macSelection == [1]):
            print("\nBot: Yasss!!! I won!! \nYou lost! Try again!. Thank you so much for playing")
        elif (macSelection == [2]):
            print("\nBot: Noooo! I lost!! aww! I'll win next time!\nYou've won!. Thank you so much for playing")            
    else:
        print("\nPlease try again")




