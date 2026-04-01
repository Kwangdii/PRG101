my_list = [1, 2, 3, "Hello", 3.14, True]
my_repeated_list = ["Hello"]*3
print(my_list)

print(type(my_list))
print(my_repeated_list)

print(my_list[1])# Accessing the second element of the list (index starts at 0)

my_list.append("Hi Karma wangdi") # Adding a new element to the end of the list
print(my_list)

my_list.extend([4,5,6,7]) # Adding multiple elements to the end of the list using extend() method
print(my_list)

my_list.insert(0, "Start") # Inserting an element at a specific index (index 0 in this case)
print(my_list)

my_list.remove(3) # Removing the first occurrence of the value 3 from the list
print(my_list)

my_list.pop() # Removing the last element from the list
print(my_list)

del my_list[-1] # Deleting the last element of the list using del statement
print(my_list)

my_repeated_list.clear() # Clearing all elements from the list
print(my_repeated_list)
