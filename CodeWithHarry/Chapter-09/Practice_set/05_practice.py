'''
Q.  Repeat program 4 for a list of such words to be censored.

'''
# Replace here words
words = ["donkey","dog","monkey","bad"]

# Open file read mode
with open("list.txt","r") as f:
    reading = f.read()
   
# Replace words
for word in words:
    reading = reading.replace(word,"#" * len(word))


with open("list.txt","w") as f:
    f.write(reading)
   

