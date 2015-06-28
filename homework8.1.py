class Animal:
    def __init__(self, name):
        self.name = name
    def define_clues(self, *clues):
        self.clues = clues
    def guess_who_am_i(self):
        print("I will give you 3 hints, guess what animal I am\n")
        for clue in self.clues:
            print(clue)
            guess = input("Who am i?:")
            if guess == self.name:
                print("You got it! I am a {}\n".format(self.name))
                return
            else:
                print("Nope, try again!\n")
        print("I'm out of hints! The answer is: {}\n".format(self.name))

e = Animal("elephant")
t = Animal("tiger")
b = Animal("bat")

e.define_clues("I have eceptional memory", "I am the largest land-living mammal in the world", "I am grey in color")
t.define_clues("I am the biggest cat", "I come in black and white or orange and black", "I can run up to 40 mph")
b.define_clues("I use echo-location", "I can fly", "I see well in the dark")

e.guess_who_am_i()
t.guess_who_am_i()
b.guess_who_am_i()
