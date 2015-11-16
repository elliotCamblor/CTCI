from collections import deque
import math

class Animal:
    def __init__(self, name):
        self.name = name
        self.order = 0

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)

class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)

class AnimalQueue():
    def __init__(self):
        self.dogs = deque()
        self.cats = deque()
        self.order = 0

    def enqueue(self, animal):
        animal.order = self.order
        self.order += 1

        if isinstance(animal, Dog):
            self.dogs.append(animal)
        else:
            self.cats.append(animal)
        
    def dequeueDog(self):
        return self.dogs.popleft()

    def dequeueCat(self):
        return self.cats.popleft()

    def dequeueAny(self):
        orderDog = self.dogs[0].order if self.dogs else math.inf
        orderCat = self.cats[0].order if self.cats else math.inf

        return self.dequeueDog() if orderDog < orderCat else self.dequeueCat()

if __name__ == "__main__":
    animalShelter = AnimalQueue()
    animalShelter.enqueue(Cat("Spotty"))
    animalShelter.enqueue(Dog("Max"))
    animalShelter.enqueue(Cat("Jack"))
    animalShelter.enqueue(Dog("Adam"))

    assert(animalShelter.dequeueAny().name == "Spotty")
    assert(animalShelter.dequeueCat().name == "Jack")
    assert(animalShelter.dequeueDog().name == "Max")

    print("success")
