#1. Write a function in python to read the content from a text file "poem.txt" line by line and display the same on screen. Solution
def readText():
    with open('/mnt/c/Users/julio/Documents/UPYprogramming/Programasdecontroleiterativos/story.text') as text:
        for line in text:
            print(line)
            
    text.close()
#2. Write a function in python to count the number of lines from a text file "story.txt" which is not starting with an alphabet "T".
def countT():
    with open('/mnt/c/Users/julio/Documents/UPYprogramming/Programasdecontroleiterativos/story.text') as text:
        count = 0
        for line in text:
            if line[0] == "T" or line[0] == "t":
                count += 1
        print("The text has "+ str(count) + " lines that start with 't'.")
    text.close()
#3. Write a function in Python to count and display the total number of words in a text file.
def countWords():
    with open('/mnt/c/Users/julio/Documents/UPYprogramming/Programasdecontroleiterativos/story.text') as text:
        count = 0
        for line in text:
            count += len(line.split())
        print("The text has " + str(count)+ " words.")
#4. Write a function in Python to read lines from a text file "notes.txt". Your function should find and display the occurrence of the word "the".
def countThe():
    with open('/mnt/c/Users/julio/Documents/UPYprogramming/Programasdecontroleiterativos/story.text') as text:
        count = 0
        a = "The"
        b = "the"
        for line in text:
            if a in line or b in line:
                count += 1
        print("The text has " + str(count) +  " 'the' words.")
    text.close()
#call the functions
readText()
countT()
countWords()
countThe()
