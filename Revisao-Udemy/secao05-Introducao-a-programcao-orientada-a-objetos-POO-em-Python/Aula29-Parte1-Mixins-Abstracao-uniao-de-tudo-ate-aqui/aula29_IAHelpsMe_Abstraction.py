from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def drive(self):
        pass

class Car(Vehicle):
    def drive(self):
        print("Driving a car")

# v = Vehicle()  # Isso resultará em erro, pois Vehicle é abstrata
c = Car()
c.drive()  # Saída: Driving a car