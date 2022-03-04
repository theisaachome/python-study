

#  create new class (new data type)

class Dog:

    def __init__(self,name) :
        self.name=name;

    def makeSound(self):
        return " I m trying to make sound..." + self.name;

    def bark(self):
        print("Bark...");


#  create an instance of the Dog
dog = Dog(name="Isaac Home");
dog.bark();
print(dog.makeSound());
print(type(dog))