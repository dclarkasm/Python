def count_frequency(alist):
    d={}
    for i in alist:
        d.update({i:d.get(i,0)+1})
    return d

mlist = ["one", "two","eleven",  "one", "three", "two", "eleven", "three", "seven", "eleven"]
print(count_frequency(mlist))
