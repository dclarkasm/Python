import os

#use path: C:\Users\Devon\Documents\UNH\2. Graduate\Semester 1\Script Programing\Python - HW Code
path = input("Please input the file path you wish to work from: ")
print("path is: " + path)

#use file name: hw4-testdoc.txt
fname = input("Please input the file name: ")

def traverse_directory(pt, fileN):
    try:
        file_r = open(pt+"\\"+fileN, 'r')
        print("opened " + fileN)
        lRead = file_r.readlines()
        file_r.close()  #close the file right after we are done with it
        for string in lRead:
            splitStr = string.split(" ")
            for word in splitStr:
                if word == 'password'+'=':
                    print("Found security hazard in file at line: " + string)
    except IOError:
        print("Error opening " + fileN + " for reading.\n")

os.chdir(path)
traverse_directory(os.getcwd(), fname)
