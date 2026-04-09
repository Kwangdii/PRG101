'''name=input("Enter your name:")
for i in name: #for loop to iterate through each character in the name
    print(i)

lenli=len(li)
for x in range(lenli):
    print(li[x]) '''

li=["Python Programming","Python Fundamentals","Python Interview Questions"]
for x in li: #for loop to iterate through each item in the list
    print(x)    #x is the variable that takes the value of each item in the list during each iteration

new_tuple= tuple(li)
for x in new_tuple: #for loop to iterate through each item in the tuple
    print(x)    #x is the variable that takes the value of each item in the tuple during each iteration

new_set= set(li)
for x in new_set: #for loop to iterate through each item in the set
    print(x)    #x is the variable that takes the value of each item in the set during each iteration
    