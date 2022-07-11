#1. Write a function in python to read the content from a text file "poem.txt" line by line and display the same on screen. Solution
def readFile():
    with open('/mnt/c/Users/julio/Documents/UPYprogramming/Programasdecontroleiterativos/story.text', 'r') as f:
        filecontent = f.read()
        print(filecontent)
        f.seek(0)
#2. Write a function in python to count the number of lines from a text file "story.txt" which is not starting with an alphabet "T".
def notTLines():
    with open('/mnt/c/Users/julio/Documents/UPYprogramming/Programasdecontroleiterativos/story.text', 'r') as f:
        i = 0
        for line in f:
            if line[0].lower() == "t":
                i += 1
        print("Text has "+ str(i) + " lines that DO NOT start with 't'.")      
    f.close()          
#3. Write a function in Python to count and display the total number of words in a text file.
def totalWords():
    with open('/mnt/c/Users/julio/Documents/UPYprogramming/Programasdecontroleiterativos/story.text', 'r') as f:
        filecontent = f.read()
        words = filecontent.split()
        print("The text has", len(words), "words!")
        
#4. Write a function in Python to read lines from a text file "notes.txt". Your function should find and display the occurrence of the word "the".
def totalThe():
    with open('/mnt/c/Users/julio/Documents/UPYprogramming/Programasdecontroleiterativos/story.text', 'r') as f:
        filecontent = f.read()
        the = ["the", "thE", "tHe", "tHE", "The", "ThE", "THe", "THE"]
        occurences = 0
        for x in the:
            occurences = occurences + filecontent.count(x)
    print("The text has " + str(occurences) +  " 'the' words.")

#5 Run all the functions!

readFile()
notTLines()
totalWords()
totalThe()