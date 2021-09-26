'''
Information and code based on notes from ECE20875 Fall 2021 @ Purdue
Adapted from material developed by Profs. Milind Kulkarni,
Stanley Chan, Chris Brinton, David Inouye, Qiang Qiu
Class Taught by: Prof Chris Brinton
Notes and Code author: Adam Piaseczny

Filter - filter is a built in function in Python. It takes one list and filters
it - creates a second list with elements that passed certain filterin criteria.
That criteria is a filter condition. The new created list is smaller (or equal to)
than the original list in size. Filter can be done with more than numeric values.
The syntax is:
    filter(filter_condition_function, data)

Map - map is a built in function in Python. It applies a certain function to all
the values in the list. It is like going through every element of a list in a loop,
and changing it, but made simplier. It has two inputs - the function that will be
applied to every element in the list, and a list that it will be applied to.
The newly created list always has the same length as the original list.
The syntax is:
    map(function_that_will_be_applied, data)

Reduce - reduce is NOT a built in function in Python. It performs a calculation on a list
and returns a single number. It does this by applying rolling computation to
sequential list of values. It needs 2 inputs - function that will be applied, and
data.
The syntax is:
(module import)
from functools import reduce
import operator
(usage)
reduce(function, data)

lambda - a notation used to make quick functions (a so called 'anonymous function')
The syntax is
    lambda input_arguments: output
'''

from functools import reduce
import operator

data = list(range(0, 10))

# Simple filter example function
def simpleFilter(data):
    # This function accepts the data, and creates a result list
    # of the filtered values. The filter condition is a number has to be odd.
    # lambda is a function that accepts 1 variable x, and returns x % 2, which is
    # 1 for odd numbers and 0 for even
    result = list(filter(lambda x: x % 2, data))
    return result

def simpleMap(data):
    # The created result list is a list of squared values from the data list
    # The lambda function accepts 1 argument - x, and return x ** 2
    result = list(map(lambda x: x ** 2, data))
    return result

def simpleReduce(data):
    # In this case it reduces the data to a single value equal to the sum of all
    # the elements in the list
    # The lambda function  accepts 2 arguments - x and y, and returns their sum
    result = reduce(lambda x, y: x + y, data)
    return result

