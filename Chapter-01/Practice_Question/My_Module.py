# Label the program written in problem 4 with comments.

# Use for print 
print("Hi! Ramanand How are you? all ok brother. ")

# This is a Built-in modules
import math
print( math.sqrt(144)) # I/O -> 12

# This is a user defined modules
def greet(name):
    return f"Hello,{name}!"

# use the module in another file
import My_Module
print(My_Module.greet("Siddharth")) # O/P -> Hello Siddharth
