'''
Q   Create a class with a class attribute a; 
    create an object from it and set ‘a’directly 
    using ‘object.a = 0’. Does this change the class
    attribute?

'''

class demo:
    a = 4


o = demo()
print(o.a) # print the class attributes because 
# instance attribute not present
o.a = 5  # instance attribute is set
print(o.a) # prints the instance attribute because
# instance Attribute present
print(demo.a) # prints the class attribetes