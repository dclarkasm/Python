def bunnyEars(b):
    if b<1:
        return b
    elif b%2==0:    #even number bunny
        print("even " + str(b))
        return bunnyEars(b-1)+2
    else:   #odd number bunny
        print("odd " + str(b))
        return bunnyEars(b-1)+3

bunnies = int(input("Please input the number of bunnies in the line: "))
print("bunnies = " + str(bunnies))
ears = bunnyEars(bunnies)
print("ears = " + str(ears))
