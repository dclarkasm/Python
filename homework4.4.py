import pickle

name = input("Please inout your name: ")
age = input("Please input your age: ")
country = input("Please input your country of origin: ")

f = open("userdata.txt", "bw")

dic = {}
dic["user"] = (name, age, country)

user_pickle = (dic)
pickle.dump(user_pickle, f)
f.close()

f = open("userdata.txt", "br")

(d) = pickle.load(f)
print(d)
f.close()
