'''
x=["melon", "apple", "banana"]

def compare_num_chars(str):
    return len(str)

print("x[1] length = " + str(compare_num_chars(x[1])))
'''

data_list=["one", "two", "three"]
for i, quote in enumerate(data_list):
    found = quote.find("t")
    if(found>=0):
        print("found")
