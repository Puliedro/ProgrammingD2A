#Exercise # 5
#Create a function where there are 2 names parameters. The first should be a greeting and the second a name.
#if the paramaters are not being passed the default values should be parameter 1 default to "Hello" parameter 2 should default to "Bob".

#Defining the function, with parameters greeting and name with default values
def greetings(greeting = "Hello", name = "Bob"):
    print(greeting, name) #printing the arguments

#Calling the function with different arguments.
greetings("ola","pris")



