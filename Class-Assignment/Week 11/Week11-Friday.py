# Write a python program to read a file line by line and store it into a list.
# Your file can contain anything, minimum 10 lines inside the txt file

def readFile(fileName):
    readAll = fileName.readlines()
    return(readAll)


fileName = open("assignment11.txt", "r")
print(readFile(fileName))