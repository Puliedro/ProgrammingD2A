#Exercise # 2

#Create a nested function to build the following:
#Using the following lists
#fruits = ("apple", "cherry", "strawberry")
#adjectives = ("big","red", "juicy")
#
#Build a function or functions to print:
#- big apple, red apple, juicy apple,
#- big cherry, red cherry, juicy cherry,
#- big strawberry, red strawberry, juicy strawberry,

#Creating a function to print an adjective and a fruit, based on an argument
def nestedFunction(a, b):
    fruits = ["apple", "cherry", "strawberry"]
    adjectives = ["big","red", "juicy"]
    print("{} {}, ".format(adjectives[b], fruits[a]), end = '')


#Making the nested loops to print all fruits and adjectives combinations
for x in range(3):
    for y in range(3):
        nestedFunction(x,y)
    print("\n")
