"""Write a program to overload the less than (<) and equal to (==) operators. For example, create objects - ob1 and ob2 with values 3 and 4 to compare values, respectively. You can additionally create more objects to try different values."""
class A:
    def __init__ (self,a):
        self.a = a
    def __lt__ (self,other):
        if self.a < other.a:
            return "ob1 is lesser than ob2"
        else:
            return "ob2 is lesser than ob1"
    def __eq__ (self,other):
        if self.a == other.a:
            return "Both are equal!"
        else:
            return "They are not equal!"
ob1 = A(5)
ob2 = A(7)
print(ob1 < ob2)

print( ob1 == ob2)