my_tuple=('Hello', 123456)
print(type(my_tuple))
print(my_tuple)

print(my_tuple[1]) # Accessing the last element of the tuple (index starts at 0)

a, b = my_tuple # Unpacking the tuple into separate variables
print(b)

new_tuple = tuple(a) # Converting a string to a tuple
print(new_tuple)

concatenated_tuple = my_tuple + new_tuple # Concatenating two tuples
print(concatenated_tuple)

print(concatenated_tuple[6:1:-4]) # Slicing the tuple to get every fourth element from index 2 to 6 and then reversing the result

print(concatenated_tuple[2:6:2]) # Slicing the tuple to get every second element from index 2 to 5

print(concatenated_tuple [1:6:-1])

'''del my_tuple
print(my_tuple) # This will raise an error because my_tuple has been deleted'''