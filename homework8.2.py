from random import randrange

print("INTEGER DIVISIONS\n(round to the nearest integer)")
while True:
    n = randrange(10)
    d = randrange(9)+1  #gaurantees that the randomly generated denomenator is greater than 0
    q = n//d

    a = input("{}/{}=".format(n, d))
    try:
        if int(a) == q:
            print("CORRECT!")
        else:
            print("INCORRECT! {}/{}={}".format(n, d, q))
    except ValueError:
        print("Please enter Integers Only!")
    except:
        print("An unknown error occured.")
