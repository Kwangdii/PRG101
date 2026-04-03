my_set={1,2,3, "Hello", 3.14,1,2, False} # Creating a set with duplicate values
print(type(my_set))
print(my_set) # output will be random because sets are unordered and do not allow duplicates

'''my_set[0] = "Start" # This will raise an error because sets are unordered and do not support indexing. Additionally, sets do not allow duplicate values, so the duplicate values will be removed when the set is created.'''

my_set.add("World") # Adding a new element to the set using add() method
print(my_set) # Output will be random because sets are unordered

my_second_set = {3, 4, 5, 'pholang'} # Creating another set
print(my_second_set) # Output will be random because sets are unordered

union_set=my_set.union(my_second_set) # Performing union of two sets
print(union_set)

intersection_set=my_set.intersection(my_second_set) # Performing intersection of two sets
print(intersection_set)

difference_set=my_set.difference(my_second_set) # Performing difference of two sets
print(difference_set)

my_second_set.clear() # Clearing all elements from the second set
print(my_second_set)