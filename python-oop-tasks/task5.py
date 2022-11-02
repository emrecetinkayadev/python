'''
Task 5

Create hierarchy out of birds.
Implement 4 classes:
* Birds class with an attribute "name" and methods "fly" and "walk".
* flying bird class with same attribute "name" and with the same methods.
Implement the method "eat" which will describe it's typical ration.
* nonflying bird class with same characteristics but which obviously will
not have the "fly".
Add same "eat" method but with other implementation regarding
the swimming bird tastes.
* a bird class which can do all of it: walk, fly, swim and eat.
But be careful which "eat" method you inherit.

Implement str() function call for each class.
'''

class Bird():
    def __init__(self, name) -> None:
        self.name = name
        
    def walk(self):
        return "Any bird can walk."
    
    def swim(self):
        return AttributeError(self, f"{self.name} object has not attribute 'swim'")
    
    def fly(self):
        raise AttributeError(f"{self.name} object has not attribute 'fly'")
    
    def eat(self):
        pass 
    
class Penguin(Bird):
    def __init__(self, name) -> None:
        super().__init__(name)
        
    def __str__(self) -> str:
        return f"{self.name} can walk and swim"
        
    def swim(self):
        return "Penguin bird can swim"
    
    def eat(self):
        return "It eats mostly fish"
    
class Canary(Bird):
    def __init__(self, name) -> None:
        super().__init__(name)
        
    def __str__(self) -> str:
        return f"{self.name} can walk and fly"
    
    def fly(self):
        return "Canary can fly."
    
    def eat(self):
        return "It eats mostly grains"
    
class SeaGull(Bird):
    def __init__(self, name) -> None:
        super().__init__(name)

    def __str__(self) -> str:
        return f"{self.name} bird can walk, swim and fly"
        
    def swim(self):
        return "Seagull can swim"
    
    def fly(self):
        return "seagull can fly"
    
    def eat(self):
        return "It eats fish"
    
    
        
# Bird
b = Bird("Any")
print(b.walk())        

# Penguin
p = Penguin("Penguin")
print(p.swim())
#p.fly()
print(p.eat())

# Canary
c = Canary("Canary")
print(str(c))
print(c.eat())

# Seagull
s = SeaGull("Gull")
print(str(s))
print(s.eat())
