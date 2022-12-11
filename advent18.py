t = [[[[4,3],4],4],[7,[[8,4],9]]]
y = [1,1]

class SnailNum:
    def __init__(self, a):
        self.a = a
        
    def reduce(self):
        print(self.a)
        for i in self.a:
            if isinstance(i,list):
                print(i)
                
    # adding two objects
    def __add__(self, o):
        self.a = [self.a , o.a]
        self.reduce()
        return self.a
        
    def __repr__(self):
        return str(self.a) 
        
t = SnailNum(t)
y = SnailNum(y)

print(t)
t=t+y
print(t)
