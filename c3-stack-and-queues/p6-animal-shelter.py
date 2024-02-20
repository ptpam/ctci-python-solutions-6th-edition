"""
Animal Shelter

Problem Statement:
An animal shelter operates on a strictly "first in, first out" basis for dogs and cats. 
People can adopt either the oldest animal at the shelter or choose between adopting the oldest dog or cat. 
Implement a system with operations such as enqueue, dequeueAny, dequeueDog, and dequeueCat, using separate queues for dogs and cats and a timestamp mechanism for tracking order.

Solution Overview:
Use separate queues for dogs and cats, each with a timestamp to track their arrival order. 
Implement methods to enqueue animals and dequeue them either by specific type (dog or cat) or any, based on which animal has been in the shelter the longest.

Solution Details:
- Maintain two queues: one for dogs and one for cats.
- Use a counter as a timestamp to mark each animal's arrival time.
- For dequeue operations, compare the timestamps of the heads of both queues to determine which animal to dequeue.

Complexity Analysis:
- Time Complexity: O(1) for all operations. Each operation performs a constant amount of work.
- Space Complexity: O(N), where N is the total number of animals in the shelter.

Solution Implementation:
"""


class Animal:
    def __init__(self, name):
        self.name = name
        self.order = None

    def set_order(self, order):
        self.order = order

    def is_older_than(self, animal):
        return self.order < animal.order


class Dog(Animal):
    pass


class Cat(Animal):
    pass


class AnimalQueue:
    def __init__(self):
        self.dogs = []
        self.cats = []
        self.order = 0

    def enqueue(self, animal):
        animal.set_order(self.order)
        self.order += 1
        if isinstance(animal, Dog):
            self.dogs.append(animal)
        elif isinstance(animal, Cat):
            self.cats.append(animal)

    def dequeueAny(self):
        if not self.dogs and not self.cats:
            return None
        if not self.dogs:
            return self.dequeueCats()
        if not self.cats:
            return self.dequeueDogs()
        dog = self.dogs[0]
        cat = self.cats[0]
        if dog.is_older_than(cat):
            return self.dequeueDogs()
        else:
            return self.dequeueCats()

    def dequeueDogs(self):
        return self.dogs.pop(0) if self.dogs else None

    def dequeueCats(self):
        return self.cats.pop(0) if self.cats else None

    def isEmpty(self):
        return len(self.dogs) == 0 and len(self.cats) == 0


# Example of usage:
if __name__ == "__main__":
    shelter = AnimalQueue()
    shelter.enqueue(Dog("Buddy"))
    shelter.enqueue(Cat("Mittens"))
    shelter.enqueue(Dog("Charlie"))
    print(shelter.dequeueAny().name)  # Buddy
    print(shelter.dequeueDogs().name)  # Charlie
    print(shelter.dequeueCats().name)  # Mittens

"""
This implementation of the AnimalQueue class provides a system for managing an animal shelter queue that operates on a "first in, first out" basis. 
It allows for the adoption of animals in the order they arrived or by selecting a specific type of animal while maintaining the order of arrival.
"""
