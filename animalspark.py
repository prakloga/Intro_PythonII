class DogPark:
    def __init__(self, dogs):
        self.dogs = dogs

    def rollcall(self):
        print("Dogs in park")
        for dog in self.dogs:
            print(dog.name)
