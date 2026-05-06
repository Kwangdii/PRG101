#fileHandler.py
'''greetings=open("hello.txt","r")
print(greetings)
greetings.close()

#to check if the file is closed or not
f=open("hello.txt","r")
print("filename:", f.name)
print("filemode:", f.mode)
f.close()
print("is this file closed?:", f.closed)

#reading the files
f=open("hello.txt","r")
contents = f.read()
print(contents)
f.close()

#writing a file
newFile=open("newFile.txt","w")
print(newFile)

#writing content to the file
newFile.write("This is a new file created by python")
newFile.close()

#file overwrite over the existing file
FileOverwrite=open("newFile.txt","w")
FileOverwrite.write("the content of the newFile is now changed ")
FileOverwrite.close()

#appending (adding at the end) a file over the existing file
appendFile=open("hello.txt","a")
appendFile.write("\n\nDon't forget to smile today!")
appendFile.close()'''

#with statement to open and close the file automatically and it is most recommended
with open("hello.txt","r") as f:
    contents=f.read()
    print(contents) #output we wil get is the content of the file hello.txt and we dont need to close the file as it will be closed automatically after the with block is executed