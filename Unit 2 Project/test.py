#Exercise # 3

#Create a function to multiply a variable list of numbers. 

#For example: a list of 5 number or a list of 10 numbers.

def product(*factors):
    k = 1
    for x in factors:
        k = k*x
    print("The product of the numbers you entered is {}".format(k))

product(2,3,4,50,7)
