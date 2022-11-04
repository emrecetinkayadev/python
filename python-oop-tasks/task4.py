'''
Task 4

Implement a Counter class which optionally accepts the start value and
the counter stop value.
If the start value is not specified the counter should begin with 0.
If the stop value is not specified it should be counting up infinitely.
If the counter reaches the stop value, print "Maximal value is reached."

Implement to methods: "increment" and "get"

'''

class Counter():
    def __init__(self, start = 0, stop = -1):
        self.start = start
        self.stop = stop
        self.current = self.start
        self.__secret = "sadasdad"
        
    def increment(self):
        if self.stop == -1:
            self.current += 1
        elif self.current < self.stop:
            self.current += 1
        else:
            print("Maximal value is reached.")
    
    @property
    def secret(self):
        return self.__secret
        
        
    
c = Counter(start=42)
c.increment()
print(c.current)

c = Counter()
c.increment()
print(c.current)

c.increment()
print(c.current)

c = Counter(start=42, stop=43)
c.increment()
print(c.current)

c.increment()

print(c.current)