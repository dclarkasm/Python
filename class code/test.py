x=2
d=1

h=d+x
#what up this is a single line comment
'''
	Heller, this is
	a double line comment
'''
print("sup world: " + str(h))

if x==d:
	print("equal")
elif x!=d:
	print("x not equal to d")
	if x>d:
		print("x is bigger than d")
	elif d>x:
		print("d is bigger than x")

a=90
while(a<=100 and a>0):
	print(a)
	a=a+1
else:
	print("Do something a the end")

name = input("what is your name? ")
print("Heller " + name + ", lets get some yum yums!")