'''
Q.  Write a program to find out the line number where python is present from quetions

'''

with open("log.txt") as f:
    lines = f.readlines()

lineno = 1
for line in lines:
    if("python" in line):
        print(f"yes python is present. Line no : {lineno}")
        break
    lineno += 1

else: 
    print("No python no present ")