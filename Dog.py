
from Predators import Animal

class Dog(Animal):

    def eat(self):
        print("dog eat bones")


d = Dog()

d.eat()
d.sounds()

