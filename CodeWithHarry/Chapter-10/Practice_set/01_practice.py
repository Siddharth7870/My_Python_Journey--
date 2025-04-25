'''
Q.  Create a class “Programmer” for storing information of few programmers 
    working at Microsoft.
'''


class programmer:
    companay = "microsof"

    def __init__(self,name,salary,language):
        self.name = name
        self.salary = salary
        self.language = language


R = programmer("Ramanand",1300000,"python")
print(R.name,R.salary,R.language,R.companay)
r = programmer("Rahul",1500000,"Java")
print(r.name,r.salary,r.language,r.companay )