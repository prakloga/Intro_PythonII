class Dog:
    scientific_name = "Canis lupus familiaris" # It's a class attribute

    def __init__(self, name):
        self.name = name
        self.woofs = 0

    def speak(self): # It's a method
        #print("woof!")
        print("Bowow!")

    def eat(self, food):
        if food == 'biscuit':
            print("Yummy!!")
        else:
            print("That's not food!!")

    #def learn_name(self, name):
    #    self.name = name

    def hear(self, words):
        if self.name in words:
            self.speak()

    def count(self):
        self.woofs += 1
        for bark in range(self.woofs):
            self.speak()

# Inheritance or sub-classing
class Chihuahua(Dog):
    origin = "Mexico"

    def speak(self):
        print("Yip!")

class TrainedChihuahua(Chihuahua):
    def do_trick(self):
        print("The Chihuahua spins in the air and turns briefly into a chicken.")

class Husky(Dog):
    origin = "Siberia"

    def speak(self):
        print("Awoooo!")

class Labrador(Dog):
    origin = "Canada"

    def speak(self):
        print("Woof!")
