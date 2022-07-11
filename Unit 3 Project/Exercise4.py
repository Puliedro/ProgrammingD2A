#Exercise # 4
#Create a function to print the data type for each lenght arguments being passed.
#For example: parameter list (1, "banana", ["cherry","mango"],True)


def dataType(args):
    for x in args: #Printing the data type of every element in the tuple
        print(x, type(x))

parameterList = (1, "banana", ["cherry","mango"],True)

dataType(parameterList) #Calling the function
