import os

#use path: C:\Users\Devon\Documents\UNH\2. Graduate
path = input("Please input the file path you wish to work from: ")
print("path is: " + path)

#use file name: hw4-testdoc.txt
fname = input("Please input the file name: ")
print("file name is: " + fname)

def traverse_directory(pt, fileN):
    for root, dirs, files in os.walk(pt):
        for f in files:
            if f == fileN:
                print("found result: " + root + '\\' + f)   

os.chdir(path)
traverse_directory(os.getcwd(), fname)
