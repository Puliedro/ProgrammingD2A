
#888     888 888b    888 8888888 88888888888       .d8888b.       8888888888 Y88b   d88P        d8888 888b     d888 
#888     888 8888b   888   888       888          d88P  Y88b      888         Y88b d88P        d88888 8888b   d8888 
#888     888 88888b  888   888       888                 888      888          Y88o88P        d88P888 88888b.d88888 
#888     888 888Y88b 888   888       888               .d88P      8888888       Y888P        d88P 888 888Y88888P888 
#888     888 888 Y88b888   888       888           .od888P"       888           d888b       d88P  888 888 Y888P 888 
#888     888 888  Y88888   888       888          d88P"           888          d88888b     d88P   888 888  Y8P  888 
#Y88b. .d88P 888   Y8888   888       888          888"            888         d88P Y88b   d8888888888 888   "   888 
# "Y88888P"  888    Y888 8888888     888          888888888       8888888888 d88P   Y88b d88P     888 888       888 


# Reversing a number using while loop in Python

# Finding the factorial of a given number using while loop

# Write a program to find the number if times the character "n" is in the string and the position number of each "n".
# For example in the following text "Ninguno sabe nadar".
# There are  4 n(s) and they are in the following positions  [0, 2, 5, 13]

def timesN():
    characterToCount = 'n'
    lst = []

    text = input("Enter the text you want to find how much times N appear in it.")
    for position, character in enumerate(text):
        if(character == characterToCount):
            lst.append(position)

    characterCounted = text.count("n")

    print("N appears a total of " + characterCounted + "times, and appears in the following positions"+ lst)

timesN()


# Write a code to reverse your full name, first names, last names.
# For example: If your name is "Yaxkukul del Rocio Lopez-Portillo Arrigunaga"
# The result should be: "Arrigunaga Lopez-Portillo Rocio del Yaxkukul"

# Write a code to print all the names and grades of the students that passed. 
# The passing grade will be 7.
# You will get a dictionary like this:
# dict_alumnos = {"Pedro":10,"Juan":9,"José":8,"Beto":5,"Maria":7,"Julia":6}
# The result should be: {'Pedro': 10, 'Juan': 9, 'José': 8, 'Maria': 7}

# Write a code to switch a dictionary keys and values and then sort them by number.
# For example:
# alumnos_id = {"Pedro":3,"Juan":6,"José":2,"Beto":5,"Maria":1,"Julia":4}
# It should get like this: {1: 'Maria', 2: 'José', 3: 'Pedro', 4: 'Julia', 5: 'Beto', 6: 'Juan'}

