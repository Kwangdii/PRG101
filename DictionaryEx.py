userDetail= {'Id':1, 'userName': 'Jetsun'}
print(type(userDetail))
print(userDetail) 

location= dict(s= 'samtse', t='thimphu', p='paro') # Creating a dictionary using the dict() constructor with keyword arguments

print(location)

print(userDetail['userName']) # Accessing the value associated with the key 'userName' in the userDetail dictionary 
print(location.get('t'))              

userDetail['email'] = 'karma@gmail.com' # Adding a new key-value pair to the userDetail dictionary
print(userDetail)

userDetail['userName'] = 'Karma_Wangdi' # Modifying the value associated with the key 'userName' in the userDetail dictionary
print(userDetail)




del location['p'] # Deleting the key-value pair with the key 'p' from the location dictionary
print(location)

delete_value= userDetail.pop('email') # Removing the key-value pair with the key 'email' from the userDetail dictionary and returning the value
print(delete_value)
      
del_key, del_value = userDetail.popitem() # Removing the key-value pair with the key 'email' from the userDetail dictionary and returning the value
print(f'the delated key is {del_key} and the deleted value is {del_value}')

'''location.clear() # Clearing all key-value pairs from the location dictionary
print(location)'''