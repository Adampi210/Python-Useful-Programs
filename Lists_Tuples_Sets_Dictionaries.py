'''
Lists, Tuples, Sets, and Dictionaries are four basic collection data types. All of
these structures can be nested.

Lists - ordered, changable, and allow duplicates. To access its values one can use
integers, or a range of indexes. Can be traversed back and forth

Tuples - ordered, unchangable, and allow duplicates. Similar to lists but the data
cannot be changed after tuple is declared. Useful if we dont want to change values
as well as we want to access a data set faster (tuples are faster than the lists).
Indexing works the same way as in lists

Sets - unordered, (half)changable (cannot change current items, but can add new,
and remove old), and DO NOT ALLOW duplicates. Indexes cannot be acccessed, but
set can be looped through to see all the values. Sets have different operations.

Dictionaries - ordered, changable, and indexed. Uses curly brackests {} like set, but
has keys and values. Keys are used to reference values, and values can be different things
(values can  be dictionaries themselfes).
'''
def ex_list():
    example_list = [0, 1, 2, 3, 4, 5, 6]
    # print(example_list[0:4]) # prints values on indexes from 0 to 3 including (or 4 excluding)
    # print(example_list[4:1:-1]) # this reverses a list and prints part of it ([4, 3, 2])
    # example_list = list(range(x)) # this creates a list of values from 0 to x - 1 inclusive
    # len(example_list) - returns length of the list (7 in that case)
    # example_list.append(x) - appends a specified element at the end of the list
    # example_list.insert(1, x) - adds element x into index 1, and shifts all elements to the right left
    # example_list.pop(n) - removes nth element from the list and returns it,
    # example_list.remove(x) - removes element with value x from the list

def ex_tuple():
    example_tuple = tuple(range(7)) # tuple creation
    # alternative declaration tuple = (0, 1, 2, 3, 4, 5, 6)
    # tuple with one item needs coma.
    # if x in example_tuple - checks if element is in a tuple
    # example_tuple.count(x) - counts number of x's in a tuple
    # example_tuple.index(x) - returns index of first x value

def ex_set():
    set1 = set(range(7))
    set2 = {1, 'a', 2, 'b'}
    # alternative declaration: set = {0, 1, 2, 3, 4, 5, 6} - will not be ordered the same each time
    # set1.union(set2) - adds all the items from both sets ONLY ONCE (NO DUPLICATES)
    # set1.intersection(set2) - checks for all values that appear in both sets
    # set1.difference(set2) - returns all values in set1 AND NOT in set2
    # set1.issubset(set2) - checks if set1 is a subset of set 2

def ex_dictionary():
    example_dictionary = {'a': [1, 'A', 'z'], 'b': [2, 'B', 'y'], 'c': [3, 'C', 'x']}
    # print(example_dictionary['a'][0]) # prints element with index 0 in the value list of key a
    # example_dictionary['d'] = [4, 'D', 'w'] - assigning new key and values to the dictionary
    # example_dictionary.values() - returns all the values from the dictionary
    # example_dictionary.keys() - returns all the keys from the dictionary
    # example_dictionary.items() - returns pairs of keys and values
    # example_dictionary.copy() - makes a copy of the dictionary

if __name__ == "__main__":
    ex_dictionary()
