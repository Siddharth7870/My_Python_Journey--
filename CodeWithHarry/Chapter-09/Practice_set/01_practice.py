'''
1. Write a program to read the text from a given file ‘poems.txt’ and find out 
   whether it contains the word ‘twinkle’
'''  

f = open("poems.txt")
read = f.read()
word = "twinkle"
if word in read:
    print(f"{word} yes")
else:
    print(f"{word} not")

f.close()