#Exercise # 7
#Create a function to receive two paramaters, a named parameter, a positional argument and a keywaord argument.
#Call the function and print the values for each one of them
#For example:
#print(paramater1), print(parameter2), print(named argument),print(positional argument), print(keyword argument)

#Defining parameters as per instructions
def parameters(a,b,named,positional, keyword = "Value"):
    #Printing the values
    print("Values are: {}, {}, {}, 1 + 23{}, {}".format(a,b,named,positional, keyword))


#Calling the function with these values
parameters(1,2, "tostada","i", "juan")