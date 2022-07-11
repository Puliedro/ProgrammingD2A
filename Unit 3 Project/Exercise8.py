#Excersise # 8

#Using recursion. Create a game that will ask the user 4 times to guess a number. if the user gueses the number print("You have won!") if the user did not guess print("You have lost!")
#Remember usibg recursion to do this.

def recursiveGuessing(k):
    number = 5 #Number to guess
    #Asking user for input, dispkaying k as the amount of tries
    guess = int(input("Enter your guess! you have {} tries\n".format(k)))
    if guess == number:
        print("You won!")
        exit() #If the number entered is the number guessed, display win message and exit the function
    else:
        print("Wrong!")
        return recursiveGuessing(k-1) #If not, play again with 1 less try

recursiveGuessing(4) #Calling the function