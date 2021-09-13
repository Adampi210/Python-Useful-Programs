'''
Information and code based on notes from ECE20875 Fall 2021 @ Purdue
Adapted from material developed by Profs. Milind Kulkarni,
Stanley Chan, Chris Brinton, David Inouye, Qiang Qiu
Class Taught by: Prof Chris Brinton
Notes and Code author: Adam Piaseczny

Functions in Python are treated as first-class objects,
and therefore have similar properties to other data types.
1. They can be assigned to variables:
    var = funcname
    var(i) = funcname(i)

2. They can have other functions as arguments:
    def main(func, var):
        result = func(var)
        return result

3. They can be returned by other functions:
    def function2(a, b):
        if a % b:
            return function0
        else:
            return function1

This flexibility allows for a lot of useful usages.
Python built-in higher order functions are for example: filter, map, reduce
The rest of this file shows great example of creating and using Higher Order Functions
'''

data = list(range(0, 1000))

'''
Let's say we want to create a function that will make a new list from data of
values between a and b. We could write a function this way:

def makeFilteredList(data, low, high):
    result = []
    for d in data:
        if d >= low and d <= high:
            result.append(d)
    return result

This however is very inefficient, because what if we wanted a function that
shows all the values not in the range? We would have to create a new function that
would do that. Instead we can create a compare fucntion, and then higher order function:
'''

def createRange(low, high):
    # This function will create other functions that will check if data_value is in range low and high
    def function_p(data_value):
        # The created function will accept one value and return True if it is in a specified range
        # and False otherwise
        if data_value <= high and data_value >= low:
            return True
        else:
            return False
    # The function returns created function
    return function_p

def makeFilteredList(data, function_p):
    # This function makes a filtered list of values from data that are in a range specified in the
    # function_p passed in argument
    result = []
    for variable in data:
        # For every value in data list the loop calls function_p with that value
        # function_p returns True if the variable is in specified range
        if function_p(variable):
            # And if it is, it is appended to the result list
            result.append(variable)
    # Finally result is returned
    return result

# Now we have all we need, we can create some ranges and call the functions

function_p1 = createRange(10, 50)
function_p2 = createRange(60, 65)

# print(function_p1(8)) # this checks if the function works, as we can see, 8 is not in the range 10 - 50 (ex 50)
# print(function_p2(63)) # this also works, since 63 is in the range of p2

nums_in_range_1 = makeFilteredList(data, function_p1) # This will return all numbers from data that are in the
# range of function p1
# print(len(nums_in_range_1)) # this would how many numbers from data are in the range of p1
nums_in_range_2 = makeFilteredList(data, function_p2) # Returns all numbers from data in range specified for p2
# print(nums_in_range_2) # this would print all the numbers in a given range
nums_in_range_3 = makeFilteredList(data, createRange(100, 150)) # We can skip the assigning functions step

# There can be mutliple functions as arguments:

def createAnd(function_1, function_2):
    # Returns a function that will look if input_variable gives true in both functions f1 and f2 from the input
    def function_p(input_variable):
        # Returns 1 if both functions are true and 0 otherwise
        return function_1(input_variable) and function_2(input_variable)
    # Comparing (or criteria checking function is created)
    return function_p

def keepEven(input_variable):
    # Returns true if input_variable is even
    return (input_variable % 2 == 0)

if_inRange_andEven = createAnd(keepEven, createRange(20, 30))
# print(if_inRange_andEven(22)) # Prints True because 22 is even and between 20 and 30
# print(if_inRange_andEven(18)) # Prints False because 18 is not in range [20,30]
# print(if_inRange_andEven(25)) # Prints False because 25 is not even

# if_inRange_andEven can be used itself in different functions, for example in
# makeFilteredList it would return all the even values in a certain range
print(makeFilteredList(data, if_inRange_andEven)) # Returns values from Data that
# are in range, and are even

# The functions can also have OR logic
# Also a function can check if a list of functions contains functions that all return true
# Example below:

def createAndL(functions_list):
    # creates a function p that checks for a given variable if all the functions in
    # function_list return true
    def function_p(variable):
        # First result is set to True
        result = True
        # Then every function is checked if it's true by doing and operation with result
        for function in function_list:
            result = result and function(variable)
        return result
    # The compare function is returned in the end, and can be called for different variables
    return function_p

# Similarly, we can create a function that will check if at least one function is true
# for a given variable from a function list

def createOrL(functions_list):
    # creates a function p that checks for a given variable if all the functions in
    # function_list return true
    def function_p(variable):
        # Instead of setting the result to True, it is set to False
        result = False
        for function in function_list:
            # If any of the functions returns true, result becomes true
            result = result or function(variable)
        # result is returned
        return result
    # comparing function is returned
    return function_p
