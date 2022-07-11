#Excersise # 6
#Create a function where you use 2 paramaters, a positional argument and a named parameter set it to True as a defaut value.
#Pass 2 numbers in each parameter wich you will add to a positional argument number list only if the named paramater is True.
#The function performs addition operation if option is True. Since the default value is True, the function returns the sum of the arguments unless option parameter is declared as False.
#Test your function with the following data:
#a = 10
#b = 20
#lst(10,20,30,40,50)
#Do not pass the third paramater
#Same as before and now pass option = False (option will be the third parameter)


#Defining the function and arguments. boolean is True as per default
def exercise6(a,b,bool=True):
    lst = [10,20,30,40,50] #declaring a list
    if bool == True:
        sum = a+b
        lst.append(sum) #Making the sum of the 2 numbers and adding them to the list
    print(lst)

#Calling the function
exercise6(420,69)
exercise6(420,69, False)