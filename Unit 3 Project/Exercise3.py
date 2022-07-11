#Exercise # 3

#Create a function to multiply a variable list of numbers. 

#For example: a list of 5 number or a list of 10 numbers.

#Function to multiply all factors in a list
def product(factors):
    k = 1
    for x in factors:
        k = k*x
    print("The product of the numbers you entered is {}".format(k))

#Declaring an empty list
fact = []
#Declaring a placeholder for an user decision
y = 1

#While loop as long as y = 1, based on user input if they want to continue adding numbers
while y == 1:
    f = input("Enter a factor!\n")
    fact.append(int(f)) #Adding the number entered to the list
    next = input("Do you want to continue? Type anything to continue or No to multiply the numbers entered!\n")
    if next.lower() == "no":
        y = 0
#Printing the numbers entered
print("Multiplication of ", fact)

#Calling the function with our list as an argument
product(fact)