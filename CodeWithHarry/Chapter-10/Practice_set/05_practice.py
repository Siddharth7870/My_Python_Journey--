'''
Q.  Add a static method in problem 2, 
    to greet the user with hello.
    
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

    @staticmethod
    def hello():
        print("Hello There!")


# C = calculator(5)
n = int(input("Enter a number : "))
C = calculator(n)
C.hello()
C.square()
C.cube()
C.squareroot()