import os
import shelve
import pickle
from datetime import datetime

'''*********************************
MUST REMEMBER TO DELETE THE SHELVE FILES
BEFORE RUNNING OR WILL RESULT IN INACCURATE
RESULTS FOR SHELVE
*********************************'''
lRead = {}
try:
    file_r = open("hw4-testdoc.txt", 'r')
    print("opened file...\n")
    lRead = file_r.readlines()
    file_r.close()  #close the file right after we are done with it
except IOError:
    print("Error opening file for reading.\n")
    
######################################## shelve
print("\n\nShelve\n")
dtss = datetime.now()   #starting time for shelve
s = shelve.open("sTest")
for string in lRead:
    splitStr = string.split(" ")
    for word in splitStr:
        if word in s:
            s[word] = s[word] + 1
        else:
            s[word] = 1
for e in s:
    print(e + " : " + str(s[e]))
s.close()
dtes = datetime.now() #ending time for shelve
print("\n\nDictionary:\n")
dtsd = datetime.now() #starting time for dictionary

######################################## dictionary
dic = {}
for string in lRead:
    splitStr = string.split(" ")
    for word in splitStr:
        if word in dic:
            dic.update({word:dic[word]+1})
        else:
            dic.update({word:1})
for e in list(dic.keys()):
    print(e + " : " + str(dic[e]))
dted = datetime.now()   #end time for dictionary

print("\n\nShelve time: " + str(dtes-dtss))
print("Dictionary time: " + str(dted-dtsd))
