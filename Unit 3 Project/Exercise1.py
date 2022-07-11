#Exercise # 1
#Create a function that will sum two numbers and return their value and then print it



def sum(a,b): #Sum the values entered
    sum = int(a) + int(b) 
    print("\nThe sum of the two numbers is ", sum)
    print("The sum of {} and {} is {}".format(a, b, sum)) #Printing them
    print(sum)


x, y =input("\nEnter two numbers and I will add them\n").split() #Making the user input 2 values in the same line
sum(x,y)