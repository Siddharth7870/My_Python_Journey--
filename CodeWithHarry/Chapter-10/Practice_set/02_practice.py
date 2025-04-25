class calculater:
    Add = "Addition"
    Sub = "Subtraction"
    Multi = "Multiplication"
    Div = "Division"
    Rem = "Remender"

    def __init__(self,a, b):
        self.a = a
        self.b = b
       

cal = calculater(80,5)
add = cal.a + cal.b
print(f"{cal.Add} -> {cal.a} + {cal.b} = { add}")
print(f"{cal.Sub} -> {cal.a - cal.b} ")
print(f"{cal.Multi} -> {cal.a * cal.b} ")
print(f"{cal.Div} -> {cal.a / cal.b} ")
print(f"{cal.Rem} -> {cal.a % cal.b} ")
