'''
List comprehension - a simple way of creating a list in Python. It can be used
instead of using for loop, and creating the lists manually. It creates new list
based on the old list, and specified parameters as follows:
new_list = [output_expression for item in iterable if condition]
the if condition can be if else condition. Compared with for loops list comprehension
is more computationally efficient, but less flexible

'''

def ex_list_comp():
    first_list = list(range(10))
    # list_copy = [i for i in first_list] # simpliest copy of a list
    # example below of creating a new list with specified parameters
    # even_square_list = [element ** 2 for element in first_list if element % 2 == 0]
    # can also be nested
    l_many = [['3', '4', '5'], ['6', '8', '10', '12']]
    # l_many_int = [[int(i) for i in element] for element in l_many]
    # list can be flattened, but in order - first all elements need to be looped and then elements of elements
    # the below code first extracts all values (inner lists) from l_many
    # and then single values from inner lists as integers
    l_flat = [int(single_val) for value in l_many for single_val in value]
    l_descriptions = ['large' if i > 9 else 'small' for i in l_flat
                        if i % 3 == 0
                        if i % 2 == 0]
    # break lines can be used between the brackets to make it more readible
    # both ifs have to be satisfied, but or, and, etc. can also be used

if __name__ == '__main__':
    ex_list_comp()
