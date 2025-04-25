'''
Q.  Write a class “Calculator” capable of finding 
    square, cube and square root of a 
    number.
'''



class calculator :
    def __init__(self,n):
        self.n = n

    def square(self):
        print(f"The square is {self.n * self.n}")
    
    def cube(self):
        print(f"The cube is {self.n * self.n * self.n}")

    def squareroot(self):
        print(f"The squareroot is {self.n ** 1/2}")


# C = calculator(5)
n = int(input("Enter a number : "))
C = calculator(n)
C.square()
C.cube()
C.squareroot()